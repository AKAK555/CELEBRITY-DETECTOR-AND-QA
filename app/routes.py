from flask import Blueprint, render_template,request
from app.utils.image_handler import process_image
from app.utils.qa_engine import QAEngine
from app.utils.celebrity_detector import CelebrityDetector

import base64

main =Blueprint('main', __name__)
qa_engine = QAEngine()
celebrity_detector = CelebrityDetector()

@main.route('/', methods=['GET', 'POST'])
def index():
    player_info = ""
    result_img_data = ""
    user_question = ""
    answer = ""
    
    if request.method == 'POST':     
        if 'image' in request.files:
            image_file = request.files['image']
            
            if image_file:
                img_bytes, face_box = process_image(image_file)
                
                player_info, player_name = celebrity_detector.identify(img_bytes)
                
                if face_box is not None:
                    result_img_data = base64.b64encode(img_bytes).decode('utf-8')
                else:
                    player_info = "No face detected. Please try again with a different image."
                
        
        elif "question" in request.form: 
            user_question = request.form['question']
            player_name = request.form["player_name"]
            player_info = request.form["player_info"]
            result_img_data = request.form["result_img_data"]
            
            answer = qa_engine.ask_about_celebrity(player_name, user_question)
        
    return render_template(
        "index.html",
        player_info=player_info,
        result_img_data=result_img_data,
        user_question=user_question,
        answer=answer
    )