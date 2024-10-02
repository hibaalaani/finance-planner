from django.shortcuts import render
from django import forms
# from django.http import HttpResponse
from .models import Transaction
import openai
import os
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI API with your key

# Create your views here.
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

def index (response):
    return render('<h1>hello there</h1>')

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_transactions')
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})
        
        
def view_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'view_transactions.html', {'transactions': transactions})        




def get_financial_advice(input_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Provide financial advice for the following situation: {input_text}",
        max_tokens=100
    )
    return response.choices[0].text.strip()



def financial_advice(request):
    advice = ""
    if request.method == 'POST':
        query = request.POST['query']
        advice = get_financial_advice(query)
    return render(request, 'financial_advice.html', {'advice': advice})
