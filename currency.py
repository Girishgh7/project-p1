import tkinter as tk 
from forex_python.converter import CurrencyRates

common_currencies=['INR','EUR','USD','AUD','NZD','AED','SAR','GBP','RUB','CHF','JPY']

class Currencyconverter:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title('Currency Converter')
        self.root.geometry('200x180')
        
        self.from_var=tk.StringVar(self.root)
        self.from_var.set('INR')
        self.from_menu=tk.OptionMenu(self.root,self.from_var,*values:*common_currencies)
        self.from_menu.pack(pady=1)
        
        self.from_var=tk.StringVar(self.root)
        self.from_var.set('USD')
        self.from_menu=tk.OptionMenu(self.root,self.from_var,*values:*common_currencies)
        self.from_menu.pack(pady=1)
        
        self.amount_label=tk.Label(self.root,text='Amount:')
        self.amount.pack(pady=1)
        
        self.amount.entry=tk.Entry(self.root)
        self.amount_entry.pack(pady=1)
        
        self.convert_button=tk.Button(self.root,text='Convert',comand=self.convert_currency)
        self.convert_button.pack(pady=1)
        
        self.reuslt_label=tk.label(self.root,text='')
        self.reuslt_label.pack(pady=1)
        
        self.root.mainloop()
        
        def convert_currency(self):
            try:
                from_currency=self.from_var.get()
                to_currency=self.to_var.get()
                amount=float(self.amount_entry.get())
                
                c_rates=CurrencyRates()
                
                rate=c_rates.get_rate(from_currency,to_currency)
                convert_amount=amount*rate
                
                self.result_label.config(text=f'{amount}{from_currency}={convert_amount:2f}{to_currency}')
            except ValueError:
                self.result_label.config(text='Please enter a valid number!')
            except Exception:
                self.result_label.config(text='Error occured')
if __name__=='__main__':
    Currencyconverter()               
                

                
        