"""Ubermelon shopping application Flask server.

Provides web interface for browsing melons, seeing detail about a melon, and
put melons in a shopping cart.

Authors: Joel Burton, Christian Fernandez, Meggie Mahnken.
"""


from flask import Flask, render_template, redirect, flash, session
import jinja2

import melons


app = Flask(__name__)

# Need to use Flask sessioning features

app.secret_key = 'this-should-be-something-unguessable'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.

app.jinja_env.undefined = jinja2.StrictUndefined


@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")


@app.route("/melons")
def list_melons():
    """Return page showing all the melons ubermelon has to offer"""

    melon_list = melons.get_all()
    return render_template("all_melons.html",
                           melon_list=melon_list)


@app.route("/melon/<int:melon_id>")
def show_melon(melon_id):
    """Return page showing the details of a given melon.

    Show all info about a melon. Also, provide a button to buy that melon.
    """


    melon = melons.get_by_id(melon_id)
    print melon
    return render_template("melon_details.html",
                           display_melon=melon)


@app.route("/cart")
def shopping_cart():
    """Display content of shopping cart."""

    # TODO: Display the contents of the shopping cart.

    # The logic here will be something like:
    #
    # - get the list-of-ids-of-melons from the session cart
    # - loop over this list:
    #   - keep track of information about melon types in the cart
    #   - keep track of the total amt ordered for a melon-type
    #   - keep track of the total amt of the entire order
    # - hand to the template the total order cost and the list of melon types


    #Already have the melon information from our get_by_id function in melons.py 
    #and would only need to get from it the melon name and price info. 
    #This way we can just count quantity and get the total 
    #.get_by_id function is only taking 1 id and my cart_ids is a list of ids

    # melons = melons.get_by_id(cart_ids)
    # # print melons

    # cart_ids = session['cart'] #bind values to the variable cart_ids   

    melon_dict = melons.get_all()

    for obj in melon_dict:
        print obj #(checkpoint) This will print every opject within the melon_dict


    melon_objects = {} #create an empty dictionary

    id = {price: melons.melon_types.price, 
        melon_name: melons.common_name, 
        quantity: int,
        total: int}

    for key, value in melon_objects.items():
        for key, value in id.items():
            if value not in id:




    # for id in cart_ids:
    #     if id not in cart_id_dict:
    #         cart_id_dict['id'] = {"quantity":1,
    #     else:
    #         cart_id_dict['id'].append(quantity)

    # if 'price' not in cart_id_dict:
    # cart_id_dict['cart_ids']['price'] = []
    # else:
    # cart_id_dict['cart_ids']['price'].append()
    # # elif 'melon name' not in cart_id_dict:
    #     cart_id_dict['cart_ids']['melon name'] = [name]
    # else:
    #     cart_id_dict['cart_ids']['melon name'].append[name]
    # elif 'quantity' not in cart_id_dict:
    #     cart_id_dict['cart_ids']['quantity'] = [amount]
    # else:
    #     cart_id_dict['cart  ds']['total'] = [value]
    # else:
    #     cart_id_dict['cart_ids']['total'].append[value]



    return render_template("cart.html")


@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):
    """Add a melon to cart and redirect to shopping cart page.

    When a melon is added to the cart, redirect browser to the shopping cart
    page and display a confirmation message: 'Successfully added to cart'.
    """
    #Session equals to an empty dictionary (session = {})

    if 'cart' not in session:
        session['cart'] = [id]
    else:
        session['cart'].append(id)

        flash("Successfully added your melon to the cart.")
    return redirect("/cart")

    # TODO: Finish shopping cart functionality

    # The logic here should be something like:
    #
    # - add the id of the melon they bought to the cart in the session



@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site.

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """

    # TODO: Need to implement this!

    return "Oops! This needs to be implemented"


@app.route("/checkout")
def checkout():
    """Checkout customer, process payment, and ship melons."""

    # For now, we'll just provide a warning. Completing this is beyond the
    # scope of this exercise.

    flash("Sorry! Checkout will be implemented in a future version.")
    return redirect("/melons")


if __name__ == "__main__":
    app.run(debug=True)
