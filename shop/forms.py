from django import forms 

from .models import Cart,Address,Order

class CartForm(forms.ModelForm):

    class Meta:
        model   = Cart
        fields  = [ "user","product","amount" ]

class ProductSortForm(forms.Form):

    #並び替えの選択肢を作る
    choices         = [
                        ("price","価格安い順"),
                        ("-price","価格高い順"),
                    ]

    #並び替えバリデーション用のフィールド
    order_by        = forms.ChoiceField(choices=choices)


class AddressForm(forms.ModelForm):
    class Meta:
        model   = Address
        fields  = [ "user","prefecture","city","address" ]


#CheckoutBeforeViewにて指定された住所をOrderモデルへ記録。
class OrderBeforeForm(forms.ModelForm):
    class Meta:
        model   = Order
        fields  = [ "user","prefecture","city","address" ]

#CheckoutViewにて、セッションIDを記録する用
class OrderSessionForm(forms.ModelForm):
    class Meta:
        model   = Order
        fields  = [ "session_id" ]

class OrderCheckoutSuccessForm(forms.ModelForm):
    class Meta:
        model   = Order
        fields  = [ "paid" ]





