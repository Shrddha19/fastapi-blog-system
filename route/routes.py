from fastapi import APIRouter,Depends,Request,Form,Response
from sqlalchemy.orm import Session
from models.table import shr
from models.table import hey
from database import sessionlocal
from fastapi.responses import HTMLResponse,RedirectResponse
from starlette .middleware.sessions import SessionMiddleware 
from werkzeug.security import generate_password_hash,check_password_hash


from fastapi import Request
from fastapi.templating import Jinja2Templates
templates=Jinja2Templates(directory="templates")


app=APIRouter()

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()
        
            
@app.get("/")

def home(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse(request,
    "home.html",
    
)
    
@app.get("/sign")
def sign(request:Request):
    return templates.TemplateResponse(request,"sign.html")  



@app.post("/sign", response_class=HTMLResponse)
def signin(request:Request,email:str=Form(...),password:str=Form(...),db:Session=Depends(get_db)):
    hash_password=generate_password_hash(password)
    
    print(hash_password)
    exist=db.query(shr).filter(shr.email==email).first()
    if exist:
        return templates.TemplateResponse(request,"sign.html", {
            "error": "User already exists"
        })
    user=shr(email=email,password=hash_password)
    db.add(user)
    db.commit()
    print(user)
    db.refresh(user)
    return RedirectResponse(url="/login" , status_code=303)


  
@app.get("/login")
def log(request:Request):

    return templates.TemplateResponse(request,"login.html")
    
@app.post("/login")
def log(request:Request,email:str=Form(),password:str=Form(),db:Session=Depends(get_db)):
    
    user=db.query(shr).filter(shr.email==email).first()
    if user and check_password_hash(user.password,password):
        print("login")
        request.session["user_id"]=user.id
        request.session["email"]=user.email
        return RedirectResponse(url="/desktop",status_code=303)
        
    return templates.TemplateResponse(request,"login.html",{"user":user})

@app.get("/desktop",response_class=HTMLResponse)
def desk(request:Request):
    user_id=request.session.get("user_id")
    if not user_id:
        return RedirectResponse(url="/home" ,status_code=303)
    
    return templates.TemplateResponse(request,"desk.html")

@app.post("/search",response_class=HTMLResponse)
def sea(request:Request,search:str=Form(...),db:Session=Depends(get_db)):
    search=db.query(hey).filter(hey.title==search).all()
    return templates.TemplateResponse(request,"searchitem.html",{"users":search})
    
    
    

@app.get("/create_blog",response_class=HTMLResponse)
def create(request:Request):
    user_id=request.session.get("user_id")
    if not user_id :
        return RedirectResponse(url="/home",status_code=303)
    return templates.TemplateResponse(request,"create.html")

@app.post("/create_blog",response_class=HTMLResponse)
def creates(request:Request,title:str=Form(...),context:str=Form(...),db:Session=Depends(get_db)):
    user_id=request.session.get("user_id")
    user=hey(title=title,context=context,user_id=user_id)
    db.add(user)
    db.commit()
    
    request.session["msg"]="Blog Created Succesfully"
    return templates.TemplateResponse(request,"create.html",{"user":user})




@app.get("/update_blog",response_class=HTMLResponse)
def update(request:Request,db:Session=Depends(get_db)):
    user_id=request.session.get("user_id")
    if not user_id:
        return RedirectResponse(url="/home",status_code=303)
    blogs=db.query(hey).filter(hey.user_id==user_id).all()
    print(blogs)
    for i in blogs:
        print(i.title)
        print(i.context)
    
    return templates.TemplateResponse(request,"update.html",{"blog":blogs})


@app.get("/update/{id}",response_class=HTMLResponse)
def change(id:int,request:Request,db:Session=Depends(get_db)):
    user_id=request.session.get("user_id")
    if not user_id:
        return RedirectResponse(url="/" ,status_code=303)
    
    blog=db.query(hey).filter(hey.id==id).first()
    return templates.TemplateResponse(request,"change.html",{"user":blog})

@app.post("/update/{id}", response_class=HTMLResponse)
def chnag(id:int,request:Request,title:str=Form(...),context:str=Form(...),bd:Session=Depends(get_db)):
    user_id=request.session.get("user_id")
    if not user_id:
        return RedirectResponse(url="/",status_code=303)
    blog=bd.query(hey).filter(hey.id==id).first()
    if blog:
        blog.title=title
        blog.context=context
        bd.commit()
    return templates.TemplateResponse(request,"change.html",{"user":blog})



@app.get("/show_blog",response_class=HTMLResponse)
def show(request:Request,db:Session=Depends(get_db)):
    user=db.query(hey).all()
    return templates.TemplateResponse(request,"show.html",{"users":user})
    

    
@app.get("/delete_blog", response_class=HTMLResponse)
def rem(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")

    demo = db.query(hey).filter(hey.user_id == user_id).all()

      # DEBUG LINE

    for i in demo:
        print(i.title)
        print(i.context)

    return templates.TemplateResponse(request,
        "delete.html",
        { "users": demo}
    )
    
@app.get("/delete/{id}",response_class=HTMLResponse)    
def dele(id:int,request:Request,db:Session=Depends(get_db)):
    demo=db.query(hey).filter(hey.id==id).first()
    return templates.TemplateResponse(request,"remove.html",{"users":demo})

@app.post("/delete/{id}",response_class=HTMLResponse)
def rem(id:int,request:Request,db:Session=Depends(get_db)):
    demo=db.query(hey).filter(hey.id==id).first()
    if demo:
        db.delete(demo)
        db.commit()
        print("deleted")
        db.close()  
    return templates.TemplateResponse(request,"remove.html",{"users":demo})

@app.get("/delete_blog",response_class=HTMLResponse)
def dele(id:int,request:Request,db:Session=Depends(get_db)):
    demo=db.query(hey).filter(hey.id==id).first()
   
        
    return templates.TemplateResponse(request,"remove.html",{"users":demo})     

@app.get("/logout")
def logout(request:Request):
    request.session.clear()
    return RedirectResponse("/",status_code=303)   