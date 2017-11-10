# from the flask library import a class named Flask
from flask import Flask

# create an instance of the Flask class
app = Flask(__name__)

# listen for a route to `/` - this is known as the root route
@app.route('/')
# when this route is reached (through the browser bar or someone clicking a link, run the following function)
def hello():
    # this `return` is the response from our server. We are responding with the text "Hello World"
    return "Hello World!"

@app.route('/name')
def name():
    return "My name is Adele"

if __name__ == "__main__":
    app.run(debug=True,port=3000)


# function firstDuplicate(a) {
#     i=0;
#     j=i+1;
#     var min = a.length
#     var answer = -1;
#     while(i < a.length-1 || j < a.length){
#         if(a[i] === a[j]){
#             if(j < min){
#                 min = j
#                 answer = a[i]
#                 i++
#                 j = i+1
#             } else {
#                 i++;
#                 j= i+1;
#             }
#         } else {
#             if(j > a.length-1){
#                 i++
#                 j = i+1
#             } else {
#                 j++
#             }
#         }
        
#     }
#     return answer
# }