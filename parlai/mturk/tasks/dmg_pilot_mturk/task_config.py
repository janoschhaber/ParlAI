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
    <div id='preview'>
        <h2> About this HIT </h2>
        <p>
            <b> You will have a conversation with another player to find out which of the six images on your display are 
                shown to the both of you - and which ones are not.
            </b> 
            <ul>
                <li> Try to identify the <i>common</i> and <i>different</i> images as fast as possible! </li>
                <li> The chat is turn-based. You can only type if it is your turn. </li>
                <li> Please use normal English language and refrain from using abbreviations or code.</li>
                <li> A full game consists of five rounds with the same partner and will take about 15 minutes. </li>
                <li> After the game, we will ask you to give us some quick feedback. </li>
                <li> If you play this game multiple times, you will get a bonus payment of 0.25 USD after each subsequent game. </li>
                <li> Every worker can play a maximum of 10 games. </li>
            </ul>
        </p>    
        
        <h2>HIT Details</h2>
        <p>
            This HIT is designed for research by Janosch Haber, under the supervision of Dr. Raquel Fernández and Dr. Elia Bruni 
            of the Dialogue Modeling Group (DMG) at the Institute of Logic, Language and Computation (ILLC) at the University of Amsterdam (UvA), the Netherlands.
            For questions, please contact <a href="mailto:dmg.illc.amsterdam@gmail.com">dmg.illc.amsterdam@gmail.com</a>.
        </p>
        <b>Payment details</b></br>
            We are aware that this is an exceptionally long HIT and want to provide fair payment. To do so, we follow the 
            following payment guidelines:
            <ul>
                <li> If a worker disconnects during the first two rounds of the game, we will automatically cancel payments for both workers </li>
                <li> If a worker disconnects during one of the later rounds, we will cancel his or her payment. The other worker receives full payment </li>
                <li> In a game, the two players can score a total of 60 points. Since this should not be a problem if you communicate well, we will 
                     automatically cancel payments for both players if the total score is below 50 points (5 mistakes each).</li>  
            </ul>
        </p>
        <p>
            <b> 
                If you accept this and are ready to play, please click "Accept" to start this task. 
            </b> </br>
            Pairing might take a moment. We will let you know once you are paired. If you turn on your speakers, 
            you will hear a sound indicating that the HIT is ready for you. 
        </p>
        <p>
            If this is the first time you are doing this HIT, we will match you with another new player and 
            start with a short warming-up round so you can get used to the game mechanics.
        </p>     
    </div>
    
    <audio id="ping" style="display:none;">
        <source src="https://raw.githubusercontent.com/janoschhaber/psivgd/master/dmg_pilot_mturk/ping.mp3" type="audio/mpeg">
        <embed height="50" width="100" src="https://raw.githubusercontent.com/janoschhaber/psivgd/master/dmg_pilot_mturk/ping.mp3">
    </audio>
    
    <div id='test'></div>
    <div id='game_window'></div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    
    <script type="text/javascript">

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
            
            required_feedback = function(fields) {
                    var valid = true;
                fields.each(function () { // iterate all
                    var $this = $(this);
                    if (($this.is(':checkbox') && !$this.is(":checked")) || // checkbox
                        ($this.is(':radio') && !$('input[name='+ $this.attr("name") +']:checked').length)) { // radio
                        valid = false;
                }
            });
                return valid;
            }

            validateRealTime_feedback = function () {
                var fields = $("form :input:not(:hidden)"); // select required
                fields.on('keyup change keypress blur', function () {
                    if (required(fields)) {
                        {document.getElementById("send_feedback").disabled = false;} // action if all valid
                    } else {
                        {document.getElementById("send_feedback").disabled = true;} // action if not valid
                    }
                });
            }
            validateRealTime_feedback();
            
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

        var game_header = "Label each image as <i>common</i> or <i>different</i> by chatting with your partner. ";
        game_header += "The number of common and different images changes every round. </br>";
        game_header += "As soon as you identify a common or different image, click the respective checkbox under the image. </br>";
        game_header += "<ul><li>Please use normal English language and refrain from using abbreviations or code.</li> ";
        game_header += "<li>Also, please do not just list descriptions of all your images.</li></ul>";
        game_header += "Remember that the chat is turn-based. If you see an hourglass, the other player is currently typing.";        
        
        var git_path = "../../../../data/dmg_full/";
        
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
                    // $('#test').html("Round: " + String(round_counter));
                    
                    if (text.startsWith('<warm-up>')) {
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
                } else if (text.startsWith('<next_round>')) {   
                } else if (text.startsWith('<feedback>')) {      
                } else if (text.startsWith('<buffer>')) { 
                    // add_to_message_buffer(cur_agent_id, "INSTRUCTOR", "Enter anything to start to next round", false);
                    // display_message_buffer(cur_agent_id);  
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
                true,
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
                true,
                true,
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
                true,
                true,
                function(msg) {}
            );
            
            add_to_message_buffer(cur_agent_id, "INSTRUCTOR", "Enter anything to start to next round", false);
            display_message_buffer(cur_agent_id); 
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
                feedback_form += 'please scroll down in this panel.</p> <form id="feedback_form"> ';
                
                feedback_form += ' <label class="statement">Overall collaboration with my partner worked well.</label> ';
                feedback_form += ' <ul class="likert"> <li> <input onclick="validateRealTime_feedback();" type="radio" name="collaboration" value="5"> ';
                feedback_form += ' <label>Strongly agree</label> </li> <li> <input onclick="validateRealTime_feedback();" type="radio" name="collaboration" value="4"> ';
                feedback_form += ' <label>Agree</label> </li> <li> <input onclick="validateRealTime_feedback();" type="radio" name="collaboration" value="3"> ';
                feedback_form += ' <label>Neutral</label> </li> <li> <input onclick="validateRealTime_feedback();" type="radio" name="collaboration" value="2"> ';
                feedback_form += ' <label>Disagree</label> </li> <li> <input onclick="validateRealTime_feedback();" type="radio" name="collaboration" value="1"> ';
                feedback_form += ' <label>Strongly disagree</label> </li> </ul>';
                
                feedback_form += ' <label class="statement">I understood the descriptions of my partner well.</label> ';
                feedback_form += ' <ul class="likert"> <li> <input onclick="validateRealTime_feedback();" type="radio" name="self_u" value="5"> ';
                feedback_form += ' <label>Strongly agree</label> </li> <li> <input onclick="validateRealTime_feedback();" type="radio" name="self_u" value="4"> ';
                feedback_form += ' <label>Agree</label> </li> <li> <input onclick="validateRealTime_feedback();" type="radio" name="self_u" value="3"> ';
                feedback_form += ' <label>Neutral</label> </li> <li> <input onclick="validateRealTime_feedback();" type="radio" name="self_u" value="2"> ';
                feedback_form += ' <label>Disagree</label> </li> <li> <input onclick="validateRealTime_feedback();" type="radio" name="self_u" value="1"> ';
                feedback_form += ' <label>Strongly disagree</label> </li> </ul>';
                
                feedback_form += ' <label class="statement">My partner seemed to understand me well.</label> ';
                feedback_form += ' <ul class="likert"> <li> <input onclick="validateRealTime_feedback();" type="radio" name="partner_u" value="5"> ';
                feedback_form += ' <label>Strongly agree</label> </li> <li> <input onclick="validateRealTime_feedback();" type="radio" name="partner_u" value="4"> ';
                feedback_form += ' <label>Agree</label> </li> <li> <input <input onclick="validateRealTime_feedback();" type="radio" name="partner_u" value="3"> ';
                feedback_form += ' <label>Neutral</label> </li> <li> <input <input onclick="validateRealTime_feedback();" type="radio" name="partner_u" value="2"> ';
                feedback_form += ' <label>Disagree</label> </li> <li> <input <input onclick="validateRealTime_feedback();" type="radio" name="partner_u" value="1"> ';
                feedback_form += ' <label>Strongly disagree</label> </li> </ul>';        
                
                feedback_form += ' <p> Do you have any comments on the HIT? <textarea id="feedback_text" name="feedback" ';
                feedback_form += ' placeholder="Input here..."> </textarea> </form>';
                feedback_form += ' <button class="btn btn-primary" disabled="disabled" style="width: 150px; font-size: 16px; float: left; margin-left: 10px; padding: 10px;" id="send_feedback" onclick="sendFeedback();"> Send Feedback </button>';
                    
                $('#game_window').html(feedback_form); 
                      
                $("button#finish").hide();  
                $("button#send_feedback").show();  
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
            $('#game_window').html("<h2>Thank You!</h2> <h3>TIP: If you continue playing, you will get a bonus payment for the next games!</h3> Please wait until the other player is done filling in the feedback form. You will then see the button to finish the HIT in the chat window.");       
                
            new_message_id = uuidv4();   
            send_packet(
                TYPE_MESSAGE,
                {
                  text: '<next_round> ' + feedback_message,
                  id: cur_agent_id,
                  message_id: new_message_id,
                  episode_done: false
                },
                true,
                true,
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


