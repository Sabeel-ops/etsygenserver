
import json
import textwrap
import google.generativeai as genai
import PIL.Image
import base64
import io
from django.shortcuts import render
from django.http import JsonResponse

# for Forbidden(CSRF cookie not set)
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def do_something(json_array):
    return_data_array = []
    
    # open received json

    first_element = json_array[0]
    target_url = first_element['url']   
    google_api_key = 'AIzaSyBlRPpSRYx9kxAZlemhEk1AT61R0-SZ5bQ'
    genai.configure(api_key=google_api_key)
    user_prompt = 'Generate etsy titles and tags for this image'
    if target_url.startswith('data:image/'):
        _, base64_data = target_url.split(',', 1)
        decoded_image = PIL.Image.open(io.BytesIO(base64.b64decode(base64_data)))
    else:    
        decoded_image = PIL.Image.open(io.BytesIO(base64.b64decode(target_url)))
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        ]
    )

    response_new = chat.send_message(["generate a single seo optimized and keyword rich and descriptive etsy title that will rank well in etsy for this personalized 16oz christian tumbler. Only generate the title",decoded_image])
    print(response_new.text)
    response_new2 = chat.send_message("the title should be longer and keyword specific.")
    print(response_new2.text)
    response_new3 = chat.send_message("only make the title keywords relatd to the design neiche, no need for keywords like forsted glass, straw and lid, etc. Print only the title")
    print(response_new3.text)
    response_new4 = chat.send_message("ok,now make it longer")
    print(response_new4.text)
    tagresp = model.generate_content(["Generate 13 SEO optimized Etsy tags separated by commas for this product that will rank well on Etsy. Do not enclose them in quotes. Each tag should not have more than 20 characters. Make the keywords related to the design and not the product details", decoded_image], stream=True)
    tagresp.resolve()
    print(tagresp.text)
    titles=response_new4.text
    tags=tagresp.text
    data = {}
    data['status'] = titles
    data['tags']=tags
    return_data_array.append(data)
  
    return return_data_array
    

@method_decorator(csrf_exempt, name='dispatch')
def get_analyzed_info(request):
    print('Request received from client')
    if request.method == 'POST':
        json_array = json.loads(request.body)

        # do something
        result = do_something(json_array)

        # send data to client 
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({'message': 'Server received GET request.', 'status': 'GET'})