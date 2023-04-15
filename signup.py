from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.Customer import Customer
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        contact = postData.get('contact')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'contact': contact,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            contact=contact,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, contact, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }

            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required !"
        elif not customer.contact:
            error_message = "Phone number is Required !"
        elif len(customer.contact) < 10:
            error_message = "Phone number is invalid !"
        elif not customer.email:
            error_message = "Email is required !"
        elif not customer.password:
            error_message = "Please enter password !"
        elif customer.isExists():
            error_message = "Email Address Already Registered"

        # saving
        return error_message