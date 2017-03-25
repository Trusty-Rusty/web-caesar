#!/usr/bin/env python

import webapp2
import caesar
import cgi

def build_page(text_area_content):
        text_label = "<label>Message to encrypt: </label>"
        text_area = "<textarea name='message'>" + text_area_content + "</textarea>"
        key_label = "<label>Encryption Key: </label>"
        key_input = "<input type='number' name='encryption_key'/>"
        button = "<input type='submit'/>"
        form = ("<form method='post'>" +
                text_label +
                text_area +
                "<br>" +
                key_label +
                key_input +
                "<br>" +
                button +
        "</form>")
        header = "<h2>Web Caesar</h2>"
        return(header + form)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(build_page(""))

    def post(self):
        message = self.request.get('message')
        key = self.request.get('encryption_key')
        encrypted_message = caesar.encrypt(message, int(key))
        escaped_message = cgi.escape(encrypted_message)
        self.response.write(build_page(encrypted_message))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
