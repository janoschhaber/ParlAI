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
        <p>
            You will be paired with another worker. Each of you then will see six images - 
            some of them are the same for both players, and some of them are only shown to one of the players.
            <b> Your task is to find out which of your images are shown to both players (common) - 
                and which are only shown to you (different)  by chatting with your partner.
            </b> 
        </p>   
        <p>
            A full game consists of five rounds with the same partner and will take about 15 minutes. 
        </p>
        <p>
            <b>QUICK INSTRUCTIONS:</b>
            <ul>
                <li> The position of an image can be different for the two players and does not matter for this task.</li>
                <li> The chat is turn-based, so you can only type if it is your turn. </li>
            </ul>
        </p>
        <p>
            <ul>
                <li> Please use correct and grammatical English and do not use abbreviations or chat language.</li>
                <li> Only mention a single image per message.</li>
                <li> Directly click on the common or different label of an image when you find out about it.</li>
            </ul>
        </p>
        <p>
            <ul>
                <li> After the game, we will ask you to give us some quick feedback.</li>
                <li> If you continue playing, you will get a bonus payment of 0.25 USD after each subsequent game.</li>
                <li> Every worker can play a maximum of 5 games.</li>
            </ul>
        </p> 
        <p>
            <b>
                If this is the first time you play, we will pair you with another new player and start with a 
                short warming-up  game. The first game therefore might take a bit longer. 
                Later games will be much quicker.
            </b>
        </p>   
        <p>
            <b>HIT DETAILS: </b> This HIT is designed for research by Janosch Haber, under the supervision of 
            Dr. Raquel Fernández and Dr. Elia Bruni of the Dialogue Modeling Group (DMG) 
            at the Institute of Logic, Language and Computation (ILLC) at the University of Amsterdam (UvA), 
            the Netherlands.
        </p>
            For questions, please contact 
            <a href="mailto:dmg.illc.amsterdam@gmail.com">dmg.illc.amsterdam@gmail.com</a>.
        </p>
     </div>
     
    <div id="onboarding_1" style="display: none;">
        <p>
            You will be paired with another worker. Each of you then will see six images - 
            some of them are the same for both players, and some of them are only shown to one of the players.
            <b> Your task is to find out which of your images are shown to both players (common) - 
                and which are only shown to you (different)  by chatting with your partner.
            </b> 
        </p>   
        <p>
            <ul>
                <li> The position of an image can be different for the two players and does not matter for this task.</li>
                <li> The chat is turn-based, so you can only type if it is your turn. </li>
            </ul>
        </p>
        <p>
            <ul>
                <li> Please use correct and grammatical English and do not use abbreviations or chat language.</li>
                <li> Only mention a single image per message.</li>
                <li> Directly click on the common or different label of an image when you find out about it.</li>
            </ul>
        </p>
        <form id="warmup_question_form">
            <p>          
                <b> QUESTION 1:</b> How do you describe images to your partner?
 
                <ul style="list-style: none;">
                    <li> <input type="radio" id="q1_a" name="q1" value="q1_a" onclick="checkQuestions();"> 
                         As many as possible in a single message. </li>
                    <li id="correct_1"> <input type="radio" id="q1_b" name="q1" value="q1_b" onclick="checkQuestions();"> 
                         One image per message. </li>
                    <li> <input type="radio" id="q1_c" name="q1" value="q1_c" onclick="checkQuestions();"> 
                         By mentioning the position on my screen. </li>
                </ul>
            <p id="answer_1"></p>
            </p> 
            <p>          
                <b> QUESTION 2: </b> When do you click the common label of an image?  
                <ul style="list-style: none;">
                    <li> <input type="radio" id="q2_a" name="q2" value="q2_a" onclick="checkQuestions();"> 
                         When I can see a similar image on my screen. </li>
                    <li> <input type="radio" id="q2_b" name="q2" value="q2_b" onclick="checkQuestions();"> 
                         When my partner has a similar image in the same position on her/his screen. </li>
                    <li id="correct_2"> <input type="radio" id="q2_c" name="q2" value="q2_c" onclick="checkQuestions();"> 
                         When my partner has the same image somewhere on her/his screen. </li>
                </ul>                
            <p id="answer_2"></p>
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
    
    <div id="onboarding_2" style="display: none;">
        <p>
            <b> A full game consists of five game rounds, but the common and different labels of an image only 
                depend on the images shown in the current round. 
            </b>            
        </p>
        <p>
            <b>EXAMPLE:</b> You see the following screen:
        </p>
        <img src='https://dmg-full.s3.eu-central-1.amazonaws.com/screen.png' width='700' style='padding:25px 50px 25px 100px'>
        <p>
            Your partner sends the following message:
        </p>
        <img src='https://dmg-full.s3.eu-central-1.amazonaws.com/message.png' width='700' style='padding:25px 50px 25px 100px'>
        <p>
            In this case you should
            <ul>
                <li> Realize that your partner probably means the middle image </li>
                <li> Mark it as common since your partner has it as well </li>
                <li> Reply to your partner that you also have that image. </li>
            </ul>
        </p>
        <p>
            <b> If you are not sure about an image described by your partner, you can also ask for more details.
            </b>
        </p>   
        <button class="btn btn-primary" style="width: 150px; font-size: 16px; float: left; margin-left: 10px; padding: 10px;" id="start_game" onclick="start_game();"> Start HIT </button>    
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
        var game_header = "Chat with your partner to find out which images are shown to the both of you <i>(common)</i> ";
        game_header += "and which ones are shown to you only <i>(different)</i>. Image positions are random and do not matter for this task.";
        game_header += "the number of <i>common</i> and different</i> <i>images changes every round. </br>";
        game_header += "Click the respective checkbox under an image to mark it as soon as you identify it as either <i>common</i> or <i>different</i> </br>";
        game_header += "<ul><li>Please use normal English language and refrain from using abbreviations or chat language.</li> ";
        game_header += "<li>Please only mention a single image per message.</li></ul>";
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
        var finish_warmup = true
                    
        function makeInput(images) {
            $('#preview').html("");
            // $('#info_button').html("<button class='btn btn-primary' style='width: 35px; border-radius: 50px;' onclick='infoMessage()'>i</button>");
            $('#game_window').html("");
            
            var display = $('#game_window');
            var string = '<form id="image_selection_form">';
        
            for (var image_id in images) {         
                var image_path = images[image_id];
        
                string += '<div class="gallery"><div class="cover" style="background-image: url(';
                string += git_path + image_path;
                string += ');"> </div> <div class="desc" ';
                string += 'id="';
                string += escapeHtml(image_path).replace(/\D/g,'');
                string += '"> <input type="radio" id="';
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
                string += '> Different </div></div>';     
            }
        
            string += ' </form>';
            string += ' <button class="btn btn-primary" style="width: 150px; font-size: 16px; float: left; margin-left: 10px; padding: 10px;" id="image_selection" onclick="getFeedback();" disabled="disabled"> Submit Selection </button>';
            string += ' <button class="btn btn-primary" style="width: 150px; font-size: 16px; float: left; margin-left: 10px; padding: 10px;" id="next_round" onclick="nextRound();"> Next Round </button>';
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
            
                if (message.images) {
                    makeInput(images);
            
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
            
                    if (num_messages == 0) {
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
                      add_to_message_buffer(cur_agent_id, "INSTRUCTOR", 'Hi! Welcome aboard. Please carefully read the instructions on the left and answer the questions to start.', false);
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
                    add_to_message_buffer(cur_agent_id, "INSTRUCTOR", "Next Round!", false);
                    display_message_buffer(cur_agent_id);
                } else if (text.startsWith('<feedback>')) {      
                } else if (text.startsWith('<waiting>')) { 
                    add_to_message_buffer(cur_agent_id, "INSTRUCTOR", "Waiting for other player to continue...", false);
                    display_message_buffer(cur_agent_id);  
                } else if (text) {
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
            $('#answer_1').html("<b>ANSWER:</b> Please only mention a single image per message so we can better process the data.")
            $('#answer_2').html("<b>ANSWER:</b> An image has the common label if it is shown to both players - independent  of its position.")
            $("button#submit_questions").hide();
            $("button#continue_warmup").show();
            jQuery("#warmup_question_form input:radio").attr('disabled',true);
        }
        
        function continue_warmup() {
            $('#onboarding_1').css("display", "none");
            $('#onboarding_2').css("display", "");        
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
                warm_up = false;
                nextRound();               
            } else {        
                $('#title').html('Feedback Form');   
               
                var feedback_form = '<h3>Please rate the following statements.</h3> ';
                feedback_form += '<p>Your input is not shown to your partner. If you do not see the submit button, '; 
                feedback_form += 'please scroll down in this panel.</p> <form id="feedback_form"> ';
                
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
            $('#game_window').html("<h2>Thank You!</h2> Please wait until the other player is done filling in the feedback form. You will then see the button to finish the HIT in the chat window. <h3>TIP: If you continue playing, you will get a bonus payment for the next games!</h3> ");       
                
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

