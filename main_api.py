# save this as app.py
from flask import Flask, render_template, redirect, url_for , request, jsonify

app = Flask(__name__, template_folder='templates')

from dotenv import load_dotenv
load_dotenv() 
  
@app.route("/") 
def home(): 
    return render_template("index.html") 

@app.route('/sendmessage', methods=['POST'])
def sendmessage():
    data = request.get_json()
    #print(data)
    
    # Process the data here
    return jsonify({"message":data['message'],"citations":[{'name':'title1','url':'url1'},{'name':'title2','url':'url2'}]})

# @app.route("/example") 
# def example(): 
#     mystr = """
#     <ul class="nav nav-tabs">
#     <li class="nav-item">
#         <a class="nav-link active" aria-current="page" href="#">Active</a>
#     </li>
#     <li class="nav-item">
#         <a class="nav-link" href="#">Link</a>
#     </li>
#     <li class="nav-item">
#         <a class="nav-link" href="#">Link</a>
#     </li>
#     <li class="nav-item">
#         <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
#     </li>
#     </ul>
#     """
#     return mystr


# @app.route("/boom1") 
# def boom1(): 
#     mystr = """<table class="table">
#   <thead>
#     <tr>
#       <th scope="col">#</th>
#       <th scope="col">First</th>
#       <th scope="col">Last</th>
#       <th scope="col">Handle</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th scope="row">1</th>
#       <td>Mark</td>
#       <td>Otto</td>
#       <td>@mdo</td>
#     </tr>
#     <tr>
#       <th scope="row">2</th>
#       <td>Jacob</td>
#       <td>Thornton</td>
#       <td>@fat</td>
#     </tr>
#     <tr>
#       <th scope="row">3</th>
#       <td colspan="2">Larry the Bird</td>
#       <td>@twitter</td>
#     </tr>
#   </tbody>
# # </table> 
# #     return mystr

# # @app.route("/boom2") 
# # def boom2(): 
# #     mystr = """<h2>Boom 2</h2>"""
# #     return mystr

  
if __name__ == "__main__": 
    app.run(debug=False) 