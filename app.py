from flask import render_template, request, flash, redirect, url_for,session, current_app
from datetime import timedelta
from passlib.hash import sha256_crypt
from flask_login import login_required,logout_user,LoginManager
from flask_uploads import IMAGES,UploadSet,configure_uploads,patch_request_class
from website import create_app
from website.forms import *
from website.models import *
from website import db
import os


basedir=os.path.abspath(os.path.dirname(__file__))
config_name = os.getenv('FLASK_CONFIG', 'default')
app = create_app(config_name)

app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir,'website/static/img')

photos = UploadSet('photos', IMAGES)
configure_uploads(app,photos)
patch_request_class(app)  

login_manager = LoginManager(app)
@login_manager.user_loader
def get_user(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None

@app.route('/')
def home():
    products=AddProduct.query.filter(AddProduct.quantity > 0)
    brands=Brand.query.all()
    return render_template("products/index.html",products=products,brands=brands)
@app.route('/brand/<int:id>')
def get_brand():
    brand=AddProduct.query.filter(brand_id=id)
    return render_template("products/index.html",brand=brand)

@app.route('/admin')
def admin():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    if 'email' not in session:
        flash(f'You must be logged in to access this page','danger')
        return redirect(url_for('login'))
    
    products=AddProduct.query.all()
    return render_template('admin/index.html',title='Admin page',products=products)

@app.route('/customerservice')
def customerservice():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    if 'email' not in session:
        flash(f'You must be logged in to access this page','danger')
        return redirect(url_for('login'))
    
    return render_template('admin/customerservice.html',title='Customer Service') 

@app.route('/stockingclerk')
def stockingclerk():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    if 'email' not in session:
        flash(f'You must be logged in to access this page','danger')
        return redirect(url_for('login'))

    products=AddProduct.query.all()
    return render_template('admin/stockingclerk.html',title='Stocking Clerk',products=products) 

@app.route('/callcenter')
def callcenter():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    if 'email' not in session:
        flash(f'You must be logged in to access this page','danger')
        return redirect(url_for('login'))
    
    return render_template('admin/callcenter.html',title='Call center') 

@app.route('/inventory')
def inventory():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    if 'email' not in session:
        flash(f'You must be logged in to access this page','danger')
        return redirect(url_for('login'))
    
    products=AddProduct.query.all()
    return render_template('admin/inventory.html',title='Call Inventory',products=products)


@app.route('/customer')
def customer():
    if 'username' not in session:
        flash(f'You must be logged in to access this page','danger')
        return redirect(url_for('customer_login'))
    products=AddProduct.query.filter(AddProduct.quantity > 0)
    brands=Brand.query.all()
    return render_template('customers/index.html',title='Customer page',products=products,brands=brands)

@app.route('/brands')
def brands():
    if 'email' not in session:
        flash(f'You must be logged in to access this page','danger')
        return redirect(url_for('login'))
    brands=Brand.query.order_by(Brand.id.desc()).all()
    return render_template('admin/brand.html',title='Brand',brands=brands)

@app.route('/category')
def category():
    if 'email' not in session:
        flash(f'You must be logged in to access this page','danger')
        return redirect(url_for('login'))
    categories=Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/brand.html',title='Brand', categories=categories)
    
@app.route('/customerdetails')
def customerdetails():
    if 'email' not in session:
        flash(f'You must be logged in to access this page','danger')
        return redirect(url_for('login'))
    else:
        customers=Customer.query.order_by(Customer.id.desc()).all()
        return render_template('admin/customer_details.html',title='Customer details', customers=customers)
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    departments= Department.query.all()
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user_data= Employee(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, department=request.form.get('department'),password=sha256_crypt.encrypt(str(form.password.data)))
        db.session.add(user_data)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title="Registration page",departments=departments)

@app.route('/login',methods=['GET', 'POST'])
def login():
    departments= Department.query.all()
    form = LoginForm(request.form)
    if request.method=="POST" and form.validate():
        employee=Employee.query.filter_by(email=form.email.data).first()

        if employee and sha256_crypt.verify(str(form.password.data),employee.password):
            session['email']=form.email.data
            if employee.department=='2':
               return redirect(url_for('callcenter'))
            elif employee.department=='3':
                return redirect(url_for('customerservice'))
            elif employee.department=='1':
                return redirect(url_for('stockingclerk'))
            else:
                 pass
        else:
            flash("Wrong password please try again",'danger')

    return render_template('admin/login.html',form=form,title="Login",departments=departments)

@app.route('/addbrand',methods=['GET', 'POST'])
def addbrand():
    if 'email' not in session:
        flash(f'You must be logged in to access this page','danger')
        return redirect(url_for('login'))
    if request.method =="POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The brand {getbrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', title='Add brand',brands='brands')

@app.route('/updatebrand/<int:id>',methods=['GET','POST'])
def updatebrand(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method =="POST":
        updatebrand.name = brand
        flash(f'The brand {updatebrand.name} was changed to {brand}','success')
        db.session.commit()
        return redirect(url_for('brands'))
    brand = updatebrand.name
    return render_template('products/updatebrand.html', title='Update brand',brands='brands',updatebrand=updatebrand)

@app.route('/deletebrand/<int:id>', methods=['POST'])
def deletebrand(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    brand = Brand.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(brand)
        flash(f"The brand {brand.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f"The brand {brand.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin'))

@app.route('/addcategory',methods=['GET', 'POST'])
def addcategory():
    if 'email' not in session:
        flash(f'You must be logged in to acces this page','danger')
        return redirect(url_for('login'))
    if request.method =="POST":
        getcategory = request.form.get('category')
        category = Category(name=getcategory)
        db.session.add(category)
        flash(f'The Category {getcategory} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addcategory'))
    return render_template('products/addbrand.html',title="Update category")

@app.route('/updatecategory/<int:id>',methods=['GET','POST'])
def updatecategory(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    updatecategory = Category.query.get_or_404(id)
    category = request.form.get('category')
    if request.method =="POST":
        updatecategory.name = category
        flash(f'The category {updatecategory.name} was changed to {category}','success')
        db.session.commit()
        return redirect(url_for('category'))
    category = updatecategory.name
    return render_template('products/updatebrand.html', title='Update category',updatecategory=updatecategory)

@app.route('/deletecategory/<int:id>', methods=['GET','POST'])
def deletecategory(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    category = Category.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(category)
        flash(f"The brand {category.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f"The brand {category.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin'))

@app.route('/addproduct',methods=['GET', 'POST'])
def addproduct():
    if 'email' not in session:
        flash(f'You must be logged in to acces this page','danger')
        return redirect(url_for('login'))
    brands=Brand.query.all()
    categories=Category.query.all()
    form =AddProducts(request.form)
    if request.method =="POST":
        name=form.name.data
        price=form.price.data
        discount=form.discount.data
        quantity=form.discount.data
        color=form.color.data
        description=form.description.data
        brand_id=request.form.get('brand')
        category=request.form.get('category')

        image_1=photos.save(request.files.get('image_1'))

        addproducts=AddProduct(name=name,price=price,discount=discount,quantity=quantity,description=description,color=color,
        brand_id=brand_id, category_id=category,image_1=image_1)

        db.session.add(addproducts)
        flash(f'The product {name} has been added to the database','success')
        db.session.commit()
        return redirect(url_for('addproduct'))
    return render_template('products/addproduct.html',form=form,brands=brands,categories=categories)

@app.route('/updateproduct/<int:id>', methods=['GET','POST'])
def updateproduct(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    form = AddProducts(request.form)
    product = AddProduct.query.get_or_404(id)
    brands = Brand.query.all()
    categories = Category.query.all()
    brand = request.form.get('brand')
    category = request.form.get('category')
    if request.method =="POST":
        product.name = form.name.data 
        product.price = form.price.data
        product.discount = form.discount.data
        product.quantity = form.quantity.data 
        product.color = form.color.data
        product.description = form.description.data
        product.category_id = category
        product.brand_id = brand
        request.files.get('image_1')
        os.unlink(os.path.join(current_app.root_path, "static/img/" + product.image_1))
               
        flash('The product was updated','success')
        db.session.commit()
        return redirect(url_for('admin'))
    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.quantity.data = product.quantity
    form.color.data = product.color
    form.description.data = product.description
    brand = product.brand.name
    category = product.category.name
    return render_template('products/updateproduct.html', form=form, title='Update Product',product=product, brands=brands,categories=categories)


@app.route('/deleteproduct/<int:id>', methods=['POST'])
def deleteproduct(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    product = AddProduct.query.get_or_404(id)
    if request.method =="POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
        except Exception as e:
            print(e)
        db.session.delete(product)
        db.session.commit()
        flash(f'The product {product.name} was deleted from ','success')
        return redirect(url_for('admin'))
    flash(f'Can not delete the product','success')
    return redirect(url_for('admin'))

@app.route('/customers/register', methods=['GET','POST'])
def customer_register():
    form=CustomerRegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user_data= Customer(first_name=form.first_name.data, last_name=form.last_name.data, username=form.username.data,
        email=form.email.data,password=sha256_crypt.encrypt(str(form.password.data)),country=form.country.data,
        city=form.city.data,contact=form.contact.data,address=form.address.data,zipcode=form.zipcode.data)
        db.session.add(user_data)
        db.session.commit()
        return redirect(url_for('customer_login'))
    return render_template('customers/register.html',form=form,title='Register')

@app.route('/customers/login',methods=['GET', 'POST'])
def customer_login():
    form = CustomerLoginForm(request.form)
    if request.method=="POST" and form.validate():
        customer=Customer.query.filter_by(username=form.username.data).first()
        if customer and sha256_crypt.verify(str(form.password.data),customer.password):
            session['username']=form.username.data
            return redirect(request.args.get('next') or url_for('customer'))
        else:
            flash("Wrong password please try again",'danger')

    return render_template('customers/login.html',form=form,title="Login")

def MagerDicts(dict1,dict2):
    if isinstance(dict1, list) and isinstance(dict2,list):
        return dict1  + dict2
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))

@app.route('/addcart', methods=['POST'])
def AddCart():
    if 'username' not in session:
        flash(f'You must be logged in to access this page','danger')
        return redirect(url_for('customer_login'))
    try:
        product_id = request.form.get('product_id')
        quantity = int(request.form.get('quantity'))
        product = AddProduct.query.filter_by(id=product_id).first()

        if request.method =="POST":
            DictItems = {product_id:{'name':product.name,'price':float(product.price),'discount':product.discount,'quantity':quantity,'image':product.image_1}}
            if 'Shoppingcart' in session:
                print(session['Shoppingcart'])
                if product_id in session['Shoppingcart']:
                    for key, item in session['Shoppingcart'].items():
                        if int(key) == int(product_id):
                            session.modified = True
                            item['quantity'] = 1
                else:
                    session['Shoppingcart'] = MagerDicts(session['Shoppingcart'], DictItems)
                    return redirect(request.referrer)
            else:
                session['Shoppingcart'] = DictItems
                return redirect(request.referrer)
              
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)

@app.route('/carts')
def getCart():
    if 'username' not in session:
        flash(f'You must be logged in to access this page','danger')
        return redirect(url_for('customer_login'))
    if 'Shoppingcart' not in session or len(session['Shoppingcart']) <= 0:
        return redirect(url_for('customer'))

    brands = Brand.query.all()
    categories = Category.query.all()
    subtotal = 0
    grandtotal = 0
    for key,product in session['Shoppingcart'].items():
        discount = (product['discount']/100) * float(product['price'])
        subtotal += float(product['price']) * 1
        subtotal -= discount
        grandtotal = float("%.2f" % (subtotal))
    return render_template('products/carts.html', grandtotal=grandtotal,brands=brands,categories=categories,title="Cart")


@app.route('/deleteitem/<int:id>',methods=['POST'])
def deleteitem(id):
    if 'Shoppingcart' not in session or len(session['Shoppingcart']) <= 0:
        return redirect(url_for('customer'))
    try:
        session.modified = True
        for key , item in session['Shoppingcart'].items():
            if int(key) == id:
                session['Shoppingcart'].pop(key, None)
                return redirect(url_for('getCart'))
    except Exception as e:
        print(e)
        return redirect(url_for('getCart'))

@app.route('/order',methods=['POST'])
def order():
     if request.method == 'POST' :
       
        return render_template('customers/order.html')

@app.route('/customerorder', methods=['GET','POST'])
def customer_order():
    form= OfflineOrderForm(request.form)
    
    return render_template('admin/create_order.html',form=form,title='Offline orders')

@app.route('/logout1')
def logout1():
    session.pop ('username',None)
    return redirect(url_for('home'))

@app.route('/logout2')
def logout2():
    session.pop ('email',None)
    return redirect(url_for('home'))


@app.errorhandler(403)
def forbidden(error):
     return render_template('errors/403.html', title='Forbidden'), 403

@app.errorhandler(404)
def page_not_found(error):
     return render_template('errors/404.html', title='Page Not Found'), 404

@app.errorhandler(500)
def internal_server_error(error):
     return render_template('errors/500.html', title='Server Error'), 500

if __name__ =='__main__':
    app.run(debug=True)
    