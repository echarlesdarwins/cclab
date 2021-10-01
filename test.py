import webapp2 
 
class MainPage(webapp2.RequestHandler): 
    def get(self): 
         self.response.write("Hello, I am Harish Kumar, Welcome to cloud computing laboratory") 
 
 
app = webapp2.WSGIApplication([('/', MainPage),],debug=True)
