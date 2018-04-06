# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.

# Code by Janosch Haber, University of Amsterdam. 2018

task_config = {}

"""A short and descriptive title about the kind of task the HIT contains.
On the Amazon Mechanical Turk web site, the HIT title appears in search results,
and everywhere the HIT is mentioned.
"""
task_config['hit_title'] = 'Detect common and different images by chatting with another player'

"""A description includes detailed information about the kind of task the HIT contains.
On the Amazon Mechanical Turk web site, the HIT description appears in the expanded
view of search results, and in the HIT and assignment screens.
"""
task_config['hit_description'] = \
    '''
    You will have a conversation with another player to find out which of the six images on your display are 
    shown to the both of you. A full game consists of five rounds and will take about 15 minutes.
    '''

"""One or more words or phrases that describe the HIT, separated by commas.
On MTurk website, these words are used in searches to find HITs.
"""
task_config['hit_keywords'] = 'chat, dialog, goal-oriented, multi-round, visually-grounded'

"""A detailed task description that will be shown on the HIT task game_window page
and on the left side of the chat page. Supports HTML formatting.
"""
task_config['task_description'] = \
    '''
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    
    <script src="https://s3.eu-central-1.amazonaws.com/dmg-full/gradient-progress-bar.js"></script>
    
    <script type="text/javascript">    
        function required(fields) {
            var valid = true;
            fields.each(function () { // iterate all
                var $this = $(this);
                if (($this.is(':checkbox') && !$this.is(":checked")) || // checkbox
                    (($this.is(':text') || $this.is('textarea')) && !$this.val()) || // text and textarea
                    ($this.is(':radio') && !$('input[name='+ $this.attr("name") +']:checked').length)) { // radio
                    valid = false;}
            });
            return valid;
        }

        function checkQuestions() {
            // $('#test').html("Validating radiobuttons");
            var fields = $("form :input:not(:hidden)"); // select required
            if (required(fields)) {
                {document.getElementById("submit_questions").disabled = false;} // action if all valid
            } else {
                {document.getElementById("submit_questions").disabled = true;} // action if not valid
            }
        }
        
        function checkFeedback() {
            //$('#test').html("Checking if feedback form is complete...");
            var fields = $("form :input:not(:hidden)"); // select required
            if (required(fields)) {
                {document.getElementById("send_feedback").disabled = false;} // action if all valid
            } else {
                {document.getElementById("send_feedback").disabled = true;} // action if not valid
            }
        }
    </script>    

    <div id='preview'>
        <b>QUICK INSTRUCTIONS:</b>
        <p>
            For this HIT you will be paired with another worker. Both of you will get a digital photo book. </br>
            Each photo book has 5 pages with 6 photos on each page. </br>
            Your photo books are different, but on each page you have some photos in common. </br>
            Each of you can only see your own photo book.
        </p>
        <p> 
            For example, you may see the page on the left, while your partner sees the page on the right 
            (for simplicity, here we use drawings rather than real photos): 
        </p>
        <img src='https://dmg-full.s3.eu-central-1.amazonaws.com/photo_icons_4.png' width='650' style='padding-left: 50px; padding-bottom: 10px'>
        <p>  
            <b> 
                Your task is to find out which of the 3 photos highlighted in yellow on your page are also shown to your partner. 
                You have to find this out by describing those highlighted photos to your partner. 
            </b>
        </p>
        <p>    
            Your partner faces the same task with different highlighted photos. 
            Therefore, to succeed, the two of you need to collaborate by chatting.
        </p>
        <p>
            <b>
                If this is the first time you play, we will pair you with another new player and start with a 
                short warming-up task. The first HIT therefore might take a bit longer. 
                Later HITs will be much quicker.
            </b>
        </p>   
        <p>
        <b>DETAILS:</b>
            <ul>
                <li> This HIT will take about 15 minutes. </li>
                <li> The chat is turn-based, so you can only type if it is your turn. </li>
                <li> Try to answer quickly so the conversation keeps flowing </li>
                <li> Please use correct and grammatical English.</li> 
                <li> Do not use abbreviations or chat language.</li>
                <li> Only describe a single photo per message so your partner doesn't get confused.</li>
                <li> Directly click on the <i>common</i> or <i>different</i> label of a photo when you find out about it.</li>
                <li> <b> If you do not follow these instructions, we retain the right to automatically cancel payment. </b> </li>
            </ul>
        </p>        
        <p>
            <ul>
                <li> After the task, we will ask you to give us some quick feedback.</li>
                <li> If you continue playing, you will get a bonus payment of 0.25 USD after each subsequent task.</li>
                <li> Every worker can play a maximum of 5 HITs.</li>
            </ul>
        </p>         
        <p>
            <b>CONTACT INFORMATION: </b> This HIT is designed for research by Janosch Haber, under the supervision of 
            Dr. Raquel Fernández and Dr. Elia Bruni of the Dialogue Modeling Group (DMG) 
            at the Institute of Logic, Language and Computation (ILLC) at the University of Amsterdam (UvA), 
            the Netherlands.
        </p>
            For questions, please contact 
            <a href="mailto:dmg.illc.amsterdam@gmail.com">dmg.illc.amsterdam@gmail.com</a>.
        </p>
     </div>
     
    <div id="onboarding_1" style="display: none;">
           <b>QUICK INSTRUCTIONS:</b>
        <p>
            For this HIT you will be paired with another worker. Both of you will get a digital photo book. </br>
            Each photo book has 5 pages with 6 photos on each page. </br>
            Your photo books are different, but on each page you have some photos in common. </br>
            Each of you can only see your own photo book.
        </p>
        <p> 
            For example, you may see the page on the left, while your partner sees the page on the right 
            (for simplicity, here we use drawings rather than real photos): 
        </p>
        <img src='https://dmg-full.s3.eu-central-1.amazonaws.com/photo_icons_4.png' width='650' style='padding-left: 50px; padding-bottom: 10px'>
        <p>  
            <b> 
                Your task is to find out which of the 3 photos highlighted in yellow on your page are also shown to your partner. 
                You have to find this out by describing those highlighted photos to your partner. 
            </b>
        </p>
        <p>    
            Your partner faces the same task with different highlighted photos. 
            Therefore, to succeed, the two of you need to collaborate by chatting.
        </p>
        <p> 
            <b>
                Your goal is to chat with your partner in order to mark the highlighted photos on your page as either 
                <i>common</i> or <i>different</i>. </br>
            </b>
        </p>
        <p>     
             In this example, the correct solution for both you and your partner would be the following: 
        </p>
        <img src='https://dmg-full.s3.eu-central-1.amazonaws.com/photo_icons_3.png' width='650' style='padding-left: 50px; padding-bottom: 10px'>
        <p>
            <b>
                Note that for common images it does not matter if they are highlighted for both players!
            </b>
        </p>
        <p>
            More concretely, assuming you see the photos below on your current page, a chat may proceed like this:
        </p>
        
        </p>
        <img src='https://dmg-full.s3.eu-central-1.amazonaws.com/new_screen.png' width='700' style='padding-left: 30px'>
        <p>
            <b> You want to find out if your partner also has the photos highlighted in yellow.</b></br>
            As an example, a chat may proceed like this: 
         </p>
        <p>  
            <b> YOU: </b> I have a photo of a little girl sleeping in a car with a teddy bear.
        </p>
        <p>   
            <b> PARTNER: </b> I have that one, too.             
        </p>
        <p>  
            <b> YOU: </b> OK
        </p>
        <p>   
            [You mark the photo as <i>common</i> and go on with the conversation]
        </p>
        <p>    
            <b> PARTNER: </b> Do you have a man on a motorcycle?
        </p>
        <p>    
            <b> YOU: </b> Yes, a red motorcycle.
        </p>
        <p>    
            <b> PARTNER: </b> Great.
        </p>
        <p>    
            [It's common, but you don't have to mark it because it is not highlighted on your page]
        </p>
        <p>    
            <b> YOU: </b> My other highlighted photo is a guy sitting on a beach with a surfboard.
        </p>
        <p>    
            <b> PARTNER: </b> I don't have the guy on the beach. 
        </p>
        <p>    
            [This time, you mark the photo as <i>different</i>]
        </p>
        <p> 
            You are done now and can click the submit button. 
            Once your partner has also submitted, you will see whether your solution was correct.
        </p>
        
        <p> 
            <b> 
                Remember that an actual photo book has 5 pages and 6 photos on each page. 
                You compare them page-by-page, so images from previous pages do not matter. 
                The order of the photos on the page also does not matter.
            </b> 
        </p>        
        <p>
        <b>DETAILS:</b>
            <ul>
                <li> The chat is turn-based, so you can only type if it is your turn. </li>
                <li> Try to answer quickly so the conversation keeps flowing </li>
                <li> Please use correct and grammatical English.</li> 
                <li> Do not use abbreviations or chat language.</li>
                <li> Only describe a single photo per message so your partner doesn't get confused.</li>
                <li> Directly click on the <i>common</i> or <i>different</i> label of a photo when you find out about it.</li>
                <li> <b> If you do not follow these instructions, we retain the right to automatically cancel payment. </b> </li>
            </ul>
        </p>
        <form id="warmup_question_form">
            <p>          
                <b> QUESTION 1: </b> What is your task in this HIT?  
                <ul style="list-style: none;">
                    <li> <input type="radio" id="q2_a" name="q2" value="q2_a" onclick="checkQuestions();"> 
                         Rearrange the highlighted photos so that they are in the same order as in my partner's book. </li>
                    <li> <input type="radio" id="q2_b" name="q2" value="q2_b" onclick="checkQuestions();"> 
                         Make a list of all highlighted photos that are in my partner's photo book. </li>
                    <li id="correct_2"> <input type="radio" id="q2_c" name="q2" value="q2_c" onclick="checkQuestions();"> 
                         Find out which highlighted photos are on the same page of my partner's photo book. </li>
                </ul>                
            <p id="answer_2"></p>
            </p>   
        
            <p>          
                <b> QUESTION 2:</b> How do you describe photos to your partner?
 
                <ul style="list-style: none;">
                    <li> <input type="radio" id="q1_a" name="q1" value="q1_a" onclick="checkQuestions();"> 
                         As many as possible in a single message. </li>
                    <li id="correct_1"> <input type="radio" id="q1_b" name="q1" value="q1_b" onclick="checkQuestions();"> 
                         One photo per message. </li>
                    <li> <input type="radio" id="q1_c" name="q1" value="q1_c" onclick="checkQuestions();"> 
                         By mentioning the position on my screen. </li>
                </ul>
            <p id="answer_1"></p>
            </p> 
            
        </form>
        
        <button class="btn btn-primary" style="width: 150px; font-size: 16px; float: left; margin-left: 10px; padding: 10px;" id="submit_questions" onclick="warmup_check_questions();" disabled="disabled"> Submit </button>
        <button class="btn btn-primary" style="width: 150px; font-size: 16px; float: left; margin-left: 10px; padding: 10px;" id="continue_warmup" onclick="continue_warmup();"> Continue </button>
        
        <script type="text/javascript">
            $("button#continue_warmup").hide();
            $('#left-pane').css("background-color", "white");
            $('#left-pane').css("padding", "0px");
            $('#left-pane').css("width", "800px"),
            $('#id_text_input').css("width", "70%");
        </script>
       </div>
    
    <div id="onboarding_3" style="display: none;">
        <p>
            <b>
            You see these instructions because this is the first time you are doing this HIT.
            As a next step, we will pair you with another new player so you can start with a short warming-up task. 
            The first HIT might therefore take a bit longer. The next ones will be much quicker because you won't get the full instructions and warming-up again.
            </b>
        </p>
        <p>
        <b> SOME MORE DETAILS: </b>
            <ul>
                <li> After the HIT, we will ask you to give us some quick feedback. </li>
                <li> If you continue playing, you will get a bonus payment of 0.25 USD after each subsequent HIT. </li>
                <li> Every worker can play a maximum of 5 HITs. </li>
            </ul>
        </p>
        <p>
            <b>PAYMENT: </b> As a task takes about 15 minutes, this HIT is much longer than the usual HIT on Mechanical Turk. 
            We want to provide fair payment for your work, but also want to make sure that the collected data is correct. 
            We therefore assess HITs based on the following criteria:
        </p>
        <p>
            <ul>
                <li> Players who do not follow the instructions will be rejected automatically without any pay. </li> 
                <li> If a worker disconnects during the first two pages, we will let the other worker return the HIT without consequences </li> 
                <li> If a worker disconnects during one of the later pages, the other worker receives full pay. </li>
                <li> The two players can score a total of 30 points. The task is collaborative, so reaching this score should be easy. We will automatically cancel payments for both players if the total score is below 24 points (3 mistakes each). </li>
            </ul>
        </p>
        <p>
            <b> If you accept this and are ready to work, please click START WARM-UP. Otherwise please return the HIT.
            </b>
            Pairing might take a moment. We will let you know once you are paired.
            If you turn on your speakers, you will hear a sound indicating that the HIT is ready for you.
        </p>   
        <button class="btn btn-primary" style="width: 150px; font-size: 16px; float: left; margin-left: 10px; padding: 10px;" id="start_game" onclick="start_game();"> Start WARM-UP </button>    
        <script type="text/javascript">
            $('#left-pane').css("background-color", "white");
            $('#left-pane').css("padding", "0px");
            $('#left-pane').css("width", "800px"),
            $('#id_text_input').css("width", "70%");
        </script>
    </div>

    <audio id="ping" style="display:none;">
        <source src="https://raw.githubusercontent.com/janoschhaber/psivgd/master/dmg_pilot_mturk/ping.mp3" type="audio/mpeg">
        <embed height="50" width="100" src="https://raw.githubusercontent.com/janoschhaber/psivgd/master/dmg_pilot_mturk/ping.mp3">
    </audio>

    <div id='test'></div>
    <div id='game_window'></div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

    <script type="text/javascript">

        function textCounter( field, maxlimit ) {
         if ( field.value.length > maxlimit ) {
          field.value = field.value.substring( 0, maxlimit );
          field.blur();
          field.focus();
          return false;
         } else {
          document.getElementById("counter").value = maxlimit - field.value.length;
         }
        }

        $(document).ready(function(){
            required = function(fields) {
                    var valid = true;
                fields.each(function () { // iterate all
                    var $this = $(this);
                    if (($this.is(':checkbox') && !$this.is(":checked")) || // checkbox
                        (($this.is(':text') || $this.is('textarea')) && !$this.val()) || // text and textarea
                        ($this.is(':radio') && !$('input[name='+ $this.attr("name") +']:checked').length)) { // radio
                        valid = false;
                }
            });
                return valid;
            }

            validateRealTime = function () {
                // $('#test').html("Validating radiobuttons");
                var fields = $("form :input:not(:hidden)"); // select required
                fields.on('keyup change keypress blur', function () {
                    if (required(fields)) {
                        {document.getElementById("image_selection").disabled = false;} // action if all valid
                    } else {
                        {document.getElementById("image_selection").disabled = true;} // action if not valid
                    }
                });
            }
            validateRealTime();

            $('#left-pane').css("background-color", "white");
            $('#left-pane').css("padding", "0px");
            $('#left-pane').css("width", "800px"),
            $('#id_text_input').css("width", "70%");
        });

    </script>

    <style>
        div.gallery {
            margin: 5px;
            border: 1px solid #ccc;
            float: left;
            width: 250px;
        }

        div.cover {
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center center;
            border: 1px solid;
            width: 250px;
            height: 167px;
        }

        div.desc {
            padding-top: 10px;
            padding-bottom: 10px;
            text-align: center;
            width: 250px;
        }

        textarea {
            width: 95%;
            height: 150px;
            padding: 12px 20px;
            box-sizing: border-box;
            border: 2px solid #ccc;
            border-radius: 4px;
            background-color: #f8f8f8;
            font-size: 16px;
            resize: none;
        }

        form .statement {
          display:block;
          font-size: 18px;
          font-weight: bold;
          padding: 10px 0 0 0%;
          margin-bottom:10px;
        }

        form .likert {
          list-style:none;
          width:100%;
          margin:0;
          padding:0 0 35px;
          display:block;
          border-bottom:2px solid #efefef;
        }

        form .likert:last-of-type {border-bottom:0;}

        form .likert:before {
          content: '';
          position:relative;
          top:11px;
          left:9.5%;
          display:block;
          background-color:#efefef;
          height:4px;
          width:78%;
        }

        form .likert li {
          display:inline-block;
          width:19%;
          text-align:center;
          vertical-align: top;
        }

        form .likert li input[type=radio] {
          display:block;
          position:relative;
          top:0;
          left:50%;
          margin-left:-6px;          
        }

        form .likert li label {width:100%;}

    </style>

    <script type="text/javascript">
        var game_header = "Chat with your partner to find out which photos are shown to both of you <i>(common)</i> ";
        game_header += "and which ones are shown to you only <i>(different)</i>. Photo positions are random and do not matter for this task. ";
        game_header += "The number of <i>common</i> and <i>different</i> photos changes every round. </br>";
        game_header += "Click the respective checkbox under a photo to mark it as soon as you identify it as either <i>common</i> or <i>different</i> </br>";
        game_header += "<ul><li>Please use normal English language and refrain from using abbreviations or chat language.</li> ";
        game_header += "<li>Please only mention a single photo per message.</li></ul>";
        game_header += "Remember that the chat is turn-based. If you see an hourglass, the other player is currently typing.";        
        
        var git_path = "https://dmg-full.s3.eu-central-1.amazonaws.com/dmg_full/";
        
        var num_messages = 0;
        var round_counter = 0;        
        var message_buffer = {}; 
        var agent_ids = new Set();       
        var names = {};
        var warm_up = false;
        var real_deal = false;
        var finished = false;
        var finish_warmup = true;
        var downloadTimer;
                    
        function makeInput(images, highlighted) {
            $('#preview').html("");
            // $('#info_button').html("<button class='btn btn-primary' style='width: 35px; border-radius: 50px;' onclick='infoMessage()'>i</button>");
            $('#game_window').html("");
            
            var display = $('#game_window');
            var string = '<form id="image_selection_form">';
            counter = 0;
            
            for (var image_id in images) {         
                var image_path = images[image_id];
                var im_high = highlighted[counter];
                counter += 1;
        
                string += '<div class="gallery"><div class="cover" style="background-image: url(';
                string += git_path + image_path;
                string += ');"> </div> <div class="desc" ';
                string += 'id="';
                string += escapeHtml(image_path).replace(/\D/g,'');
                
                 
                if (im_high) {
                    string += '" style="background-color: #f9fc6a; height:50px;">';
                    string += '<input type="radio" id="';
                    string += String(image_id);
                    string += '_common" name="';
                    string += String(image_id);
                    string += '" value="common" '
                    string += 'onclick="validateRealTime(); '            
                    string += 'sendSelectionMessage(&apos;<com>&apos;, &apos;' 
                    string += image_path 
                    string += '&apos;);"' 
                    string += '> Common <input type="radio" id="';
                    string += String(image_id);
                    string += '_different" name="';
                    string += String(image_id);
                    string += '" value="different" '
                    string += 'onclick="validateRealTime(); '            
                    string += 'sendSelectionMessage(&apos;<dif>&apos;, &apos;' 
                    string += image_path 
                    string += '&apos;);"'
                    string += '> Different'
                } else {
                    string += '" style="background-color: #d1d1d1; height:50px;">';
                }           
                  
                string += '</div></div>';     
            }        
            string += ' </form>';
            string += ' <button class="btn btn-primary" style="width: 150px; font-size: 16px; float: left; margin-left: 10px; padding: 10px;" id="image_selection" onclick="getFeedback();" disabled="disabled"> Submit Selection </button>';
            string += ' <button class="btn btn-primary" style="width: 150px; font-size: 16px; float: left; margin-left: 10px; padding: 10px;" id="next_round" onclick="nextRound();"> Next Page </button>';
            string += ' <button class="btn btn-primary" style="width: 150px; font-size: 16px; float: left; margin-left: 10px; padding: 10px;" id="finish" onclick="finishGame();"> Finish Game </button>';
             
            display.append(string);
            $("button#next_round").hide();
            $("button#finish").hide();
        }
        
        function playPing() {
            var audio=document.getElementById('ping');
            audio.play();
        }
                
        (function() {
            // Override handle_new_message function
            handle_new_message = function() {
 
                var new_message_id = arguments[0];
                var message = arguments[1];
                var agent_id = message.id;
                var text = message.text;
                var images = message.images;
                var highlighted = message.highlighted;
                var solution = message.solution;
                var was_this_agent = (agent_id == cur_agent_id);
                               
                if (agent_id && !agent_ids.has(agent_id)) {
                    agent_ids.add(agent_id);
                }      
                           
                if (displayed_messages.indexOf(new_message_id) !== -1) {
                    // This message has already been seen and put up into the chat
                    log(new_message_id + ' was a repeat message', 1);
                    return;
                }            
                log('New message, ' + new_message_id + ' from agent ' + agent_id, 1);
                displayed_messages.push(new_message_id);         
            
                if (message.images && message.highlighted) {
                    makeInput(images, highlighted);
                    startTimer();
            
                    round_counter = Number(text.split(' ').slice(1,2).join(''));
                    $('#title').html(text.split(' ').slice(0,2).join(' ')); 
                    //$('#test').html("Round: " + String(round_counter));
                    
                    if (text.startsWith('<warm-up>')) {
                        num_messages = 0;
                        round_counter = 5;
                        warm_up = true;
                        add_to_message_buffer(cur_agent_id, "INSTRUCTOR", "Since it is the first time you are playing, we will start with a small warming-up round.", false);
                    } else {
                        real_deal = true;  
                        finish_warmup = false
                    }
                    
                    //var display = $('#test').html();
                    //display += "Message: " + String(num_messages)
                    //$('#test').html(display);
            
                    if (warm_up || round_counter == 1) {
                        playPing();
                                                
                        if (message.name) {
                            names[cur_agent_id] = message.name;
                        }
                                               
                        if (warm_up && real_deal) {
                            add_to_message_buffer(cur_agent_id, "INSTRUCTOR", "Now for the real deal!", false);
                            warm_up = false;
                        } else {
                            add_to_message_buffer(cur_agent_id, "INSTRUCTOR", "You are paired with a new player, nicknamed <b>" + names[cur_agent_id] + "</b>", false);
                        }
                        
                        add_to_message_buffer(cur_agent_id, "INSTRUCTOR", game_header, false);
                        display_message_buffer(cur_agent_id)                
                    }
                                 
                } else if (text.startsWith('<hint>')) {   
                    add_to_message_buffer(cur_agent_id, "INSTRUCTOR", "Selection Submitted! Check if your partner still has got questions and answer them to continue.", false);
                    display_message_buffer(cur_agent_id)                     
                } else if (message.solution) {
                    showFeedback(solution);      
                } else if (text.startsWith('<selection>')) {  
                } else if (text.startsWith('<preview>')) {  
                      playPing();
                      add_to_message_buffer(cur_agent_id, "INSTRUCTOR", 'Hi! Welcome aboard. Please carefully read the instructions on the left and answer the questions to start. Depending on your screen size, sometimes you will need to scroll to see the buttons.', false);
                      display_message_buffer(cur_agent_id);
 
                      $('#title').html("About this HIT"); 
                      $('#preview').css("display", "none");
                      $('#onboarding_1').css("display", "");
                      num_messages = 0;
                } else if (text.startsWith('<next_round>')) {  
                } else if (text.startsWith('<pairing>')) {  
                    add_to_message_buffer(cur_agent_id, "INSTRUCTOR", "You are now paired with another player. Please stand by...", false);
                    display_message_buffer(cur_agent_id);  
                } else if (text.startsWith('<buffer>')) {   
                    add_to_message_buffer(cur_agent_id, "INSTRUCTOR", "Next Page!", false);
                    display_message_buffer(cur_agent_id);                    
                } else if (text.startsWith('<feedback>')) {      
                } else if (text.startsWith('<waiting>')) { 
                    add_to_message_buffer(cur_agent_id, "INSTRUCTOR", "Waiting for other player to continue...", false);
                    display_message_buffer(cur_agent_id);  
                } else if (text) {
                    startTimer();
                    num_messages++;
                    message.id = (was_this_agent ? "YOU:" : "THEM:");
                    var agent_id = message.id;                    
                    add_to_message_buffer(cur_agent_id, was_this_agent ? "YOU" : names[cur_agent_id], escapeHtml(text), was_this_agent);
                    display_message_buffer(cur_agent_id)
                } else {
                    $('#test').html('Message dropped through selection');
                }        
            };
        })();
        
        function warmup_check_questions() {
            $('#correct_1').css("background-color", "#8dcf8d")
            $('#correct_2').css("background-color", "#8dcf8d")
            $('#answer_1').html("<b>ANSWER: Please only mention a single photo per message so your partner doesn't get confused. </b>")
            $('#answer_2').html("<b>ANSWER: Your task is to find out which of your photos are also on the same page of your partner's book.</b>")
            $("button#submit_questions").hide();
            $("button#continue_warmup").show();
            jQuery("#warmup_question_form input:radio").attr('disabled',true);
        }
        
        function continue_warmup() {
            $('#onboarding_1').css("display", "none");
            $('#onboarding_3').css("display", "");        
        }
        
        function continue_warmup_2() {
            $('#onboarding_2').css("display", "none");
            $('#onboarding_3').css("display", "");     
        }
        
        function start_game() {
            $("button#start_game").hide();
        
            new_message_id = uuidv4();     
            send_packet(
                TYPE_MESSAGE,
                {
                  text: '<start>',
                  id: cur_agent_id,
                  message_id: new_message_id,
                  episode_done: true
                },
                false,
                false,
                function(msg) {}
            );
        }
        
        function startTimer() {        
  
            /*
          if (downloadTimer) {
            clearInterval(downloadTimer);
          }
          
          $('#progress-bar').gradientProgressBar(
            {
              value: 1.0,
              size: 400,
              fill: { gradient: ["red", "yellow", "green", "green"] },
              animation: false,
              thickness: 20
            }
          );
        
          var timeleft = 1.0;
          downloadTimer = setInterval(
            function() {
              timeleft = timeleft - (timeleft * 0.0005)
              $('.progress-bar').gradientProgressBar({ value : timeleft });
            }, 10 
          );    
          */         
        }
        
        function add_to_message_buffer(agent_id, label, text, was_this_agent){
        
            if (agent_id in message_buffer) {
                message_buffer[agent_id].push([label, text, was_this_agent]);
            } else {
                message_buffer[agent_id] = [[label, text, was_this_agent]];
            }    
        }
        
        function display_message_buffer(agent_id) {
            
            var len_buffer = message_buffer[agent_id].length;
            start = Math.max(0, len_buffer-6)
            
            clear_messages()         
            for (i = start; i < message_buffer[agent_id].length; i++) { 
                add_message_to_conversation(message_buffer[agent_id][i][0], message_buffer[agent_id][i][1], message_buffer[agent_id][i][2]);
            }        
        }
        
        function escapeHtml(unsafe) {
        
            return unsafe
                 .replace(/&/g, "&amp;")
                 .replace(/</g, "&lt;")
                 .replace(/>/g, "&gt;")
                 .replace(/"/g, "&quot;")
                 .replace(/'/g, "&#039;");
         }
        
        function sendSelectionMessage(image_id, m_type) {
        
            var selection = '<selection> ' + String(image_id) + ' ' + String(m_type)
        
            new_message_id = uuidv4();     
            send_packet(
                TYPE_MESSAGE,
                {
                  text: selection,
                  id: cur_agent_id,
                  message_id: new_message_id,
                  episode_done: false
                },
                false,
                false,
                function(msg) {}
            );
        }
        
        function showFeedback(solution) {
        
            feedback_msg = '';
        
            for (var item in solution) {    
                var item_id = item[0];
                var tuple = solution[item_id];
        
                var image_path = tuple[0];      
                var mark = tuple[1];
        
                if (mark == 1) {
                    feedback_msg += ' was correct. ';  
                    var descriptor = escapeHtml(image_path).replace(/\D/g,'');
                    $('#' + descriptor).css("background-color", "#A0FF58");
        
                } else {
                    feedback_msg += ' was NOT correct. ';
                    var descriptor = escapeHtml(image_path).replace(/\D/g,'');
                    $('#' + descriptor).css("background-color", "#FF6E65");
                }    
            } 
            
        
            if (round_counter < 5 && !warm_up) {
                $("button#next_round").show();
            } else {
                $("button#finish").show();                
                $("button#image_selection").hide();
                $("button#next_round").hide();
            }
        }
        
        function get_other_id(this_id) {
            for (let id of agent_ids) {
                if (id != this_id) {
                    return id;
                }
            }
        }
        
        function getFeedback() {
        
            jQuery("#image_selection_form input:radio").attr('disabled',true);
                                       
            new_message_id = uuidv4();  
            $("button#image_selection").hide();     
            send_packet(
                TYPE_MESSAGE,
                {
                  text: '<feedback>',
                  id: cur_agent_id,
                  message_id: new_message_id,
                  episode_done: false
                },
                false,
                false,
                function(msg) {}
            );           
        }
        
        function nextRound() {
                            
            new_message_id = uuidv4();   
            $("button#next_round").hide();  
            send_packet(
                TYPE_MESSAGE,
                {
                  text: '<next_round>',
                  id: cur_agent_id,
                  message_id: new_message_id,
                  episode_done: false
                },
                false,
                false,
                function(msg) {}
            );
            
            
        }
        
        function finishGame() {
        
            if (finish_warmup) {
                finish_warmup = false
                $("button#finish").hide();                 
                num_messages = -1;
                real_deal = true;
                nextRound();               
            } else {        
                $('#title').html('Feedback Form');   
               
                var feedback_form = '<h3>Please rate the following statements.</h3> ';
                feedback_form += '<p>Your input is not shown to your partner. If you do not see the submit button, '; 
                feedback_form += 'please scroll down in this panel. <b> It is important you submit this, otherwise you and your partner cannot finish the HIT. </b> </p> <form id="feedback_form"> ';
                
                feedback_form += ' <label class="statement">Overall collaboration with my partner worked well.</label> ';
                feedback_form += ' <ul class="likert"> <li> <input onclick="checkFeedback();" type="radio" name="collaboration" value="5"> ';
                feedback_form += ' <label>Strongly agree</label> </li> <li> <input onclick="checkFeedback();" type="radio" name="collaboration" value="4"> ';
                feedback_form += ' <label>Agree</label> </li> <li> <input onclick="checkFeedback();" type="radio" name="collaboration" value="3"> ';
                feedback_form += ' <label>Neutral</label> </li> <li> <input onclick="checkFeedback();" type="radio" name="collaboration" value="2"> ';
                feedback_form += ' <label>Disagree</label> </li> <li> <input onclick="checkFeedback();" type="radio" name="collaboration" value="1"> ';
                feedback_form += ' <label>Strongly disagree</label> </li> </ul>';
                
                feedback_form += ' <label class="statement">I understood the descriptions of my partner well.</label> ';
                feedback_form += ' <ul class="likert"> <li> <input onclick="checkFeedback();" type="radio" name="self_u" value="5"> ';
                feedback_form += ' <label>Strongly agree</label> </li> <li> <input onclick="checkFeedback();" type="radio" name="self_u" value="4"> ';
                feedback_form += ' <label>Agree</label> </li> <li> <input onclick="checkFeedback();" type="radio" name="self_u" value="3"> ';
                feedback_form += ' <label>Neutral</label> </li> <li> <input onclick="checkFeedback();" type="radio" name="self_u" value="2"> ';
                feedback_form += ' <label>Disagree</label> </li> <li> <input onclick="checkFeedback();" type="radio" name="self_u" value="1"> ';
                feedback_form += ' <label>Strongly disagree</label> </li> </ul>';
                
                feedback_form += ' <label class="statement">My partner seemed to understand me well.</label> ';
                feedback_form += ' <ul class="likert"> <li> <input onclick="checkFeedback();" type="radio" name="partner_u" value="5"> ';
                feedback_form += ' <label>Strongly agree</label> </li> <li> <input onclick="checkFeedback();" type="radio" name="partner_u" value="4"> ';
                feedback_form += ' <label>Agree</label> </li> <li> <input <input onclick="checkFeedback();" type="radio" name="partner_u" value="3"> ';
                feedback_form += ' <label>Neutral</label> </li> <li> <input <input onclick="checkFeedback();" type="radio" name="partner_u" value="2"> ';
                feedback_form += ' <label>Disagree</label> </li> <li> <input <input onclick="checkFeedback();" type="radio" name="partner_u" value="1"> ';
                feedback_form += ' <label>Strongly disagree</label> </li> </ul>';        
                
                feedback_form += ' <p> Do you have any comments on the HIT? <textarea id="feedback_text" name="feedback" ';
                feedback_form += ' placeholder="Input here..."> </textarea> </form>';
                feedback_form += ' <button class="btn btn-primary" style="width: 150px; font-size: 16px; float: left; margin-left: 10px; padding: 10px;" id="send_feedback" onclick="sendFeedback();" disabled="disabled"> Send Feedback </button>';
                    
                $('#game_window').html(feedback_form); 
                      
                $("button#finish").hide();  
                $("button#send_feedback").show();  
            }
        }
        
        function sendFeedback(){  
        
            var collaboration = $('#feedback_form').find('input[name="collaboration"]').val();
            var partner_u = $('#feedback_form').find('input[name="partner_u"]').val();
            var self_u = $('#feedback_form').find('input[name="self_u"]').val();
            var feedback_text = $('#feedback_form').find('textarea[name="feedback"]').val();
            
            var feedback_message = "col:" + String(collaboration) + "<&>partner_u:" + String(partner_u);   
            feedback_message += "<&>self_u:" + String(self_u) + "<&>text:" + String(feedback_text);    
            
            $("button#send_feedback").hide();  
            $('#game_window').html("<h2>Thank You!</h2> Please wait until the other player is done filling in the feedback form. You will then see the button to finish the HIT in the chat window. </br> <b> If the HIT took you longer than the 15 minutes we aimed at, we will compensate you through a bonus payment that is calculated based on the time spent on this HIT. </b> <h3>TIP: The next game will be much shorter because you won't get the instructions and warming-up round again - and you probably got better at it as well. PLUS: If you continue playing, you will get a bonus payment for the next games!</h3> ");       
                
            new_message_id = uuidv4();   
            send_packet(
                TYPE_MESSAGE,
                {
                  text: '<usr_feedback> ' + feedback_message,
                  id: cur_agent_id,
                  message_id: new_message_id,
                  episode_done: false
                },
                false,
                false,
                function(msg) {}
            );
        }
        
        function infoMessage(){
            var info = "Label each image as common or different by chatting with your partner. ";
            info += "The number of common and different images changes every round.";
            info += "As soon as you identify a common or different image, click the respective checkbox under the image.";
            info += "Please use normal English language and refrain from using abbreviations or code. ";
            info += "Also, please do not just list descriptions of all your images. ";
            info += "Remember that the chat is turn-based. If you see an hourglass, the other player is currently typing."; 
        
            alert(info);
        }
 
    </script>
    '''

