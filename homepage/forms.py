from django import forms
from .models import ContactForm

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'service', 'message','phone']
        widgets = {
            'name': forms.TextInput(attrs={
                    'id': 'name',
                'class': 'w-full h-11 px-4 rounded-lg border border-gray-300/50 bg-transparent focus:border-blue-500 focus:ring-1 focus:ring-blue-500 text-base transition-all duration-200 ease-out transform-gpu active:scale-[0.99] text-gray-900',
                'placeholder': 'Full Name',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'id': 'email',
                'class': 'w-full h-11 px-4 rounded-lg border border-gray-300/50 bg-transparent focus:border-blue-500 focus:ring-1 focus:ring-blue-500 text-base transition-all duration-200 ease-out transform-gpu active:scale-[0.99] text-gray-900',
                'placeholder': 'Email Address',
                'required': 'required'
            }),
          'phone': forms.NumberInput(attrs={
                'id': 'Phone',
                'class': 'w-full h-11 px-4 rounded-lg border border-gray-300/50 bg-transparent focus:border-blue-500 focus:ring-1 focus:ring-blue-500 text-base transition-all duration-200 ease-out transform-gpu active:scale-[0.99] text-gray-900',
                'placeholder': 'Phone number',
                'required': 'required',
                'maxlenght':'10',
                'minlenght':'10'
                
            }),
            
            'service': forms.Select(attrs={
                'id': 'service',
                'class': 'w-full h-11 px-4 rounded-lg border border-gray-300/50 bg-transparent appearance-none cursor-pointer text-base transition-all duration-200 ease-out transform-gpu active:scale-[0.99] text-gray-900',
                'required': 'required'
            }),
            'message': forms.Textarea(attrs={
                'id': 'message',
                'rows': 4,
                'class': 'w-full p-4 rounded-lg border border-gray-300/50 bg-transparent focus:border-blue-500 focus:ring-1 focus:ring-blue-500 resize-none text-base transition-all duration-200 ease-out transform-gpu active:scale-[0.99] text-gray-900',
                'placeholder': 'Your Message',
                'required': 'required'
            }),
        }