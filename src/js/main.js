baseUrl = "http://127.0.0.1:5000/"
bufferSlots = [
			['9:15', '9:30'],
			['13:15', '13:45'],
			['18:45', '19:00']
		]

$(document).ready(function(){
	
	// initiates the timepicker object
	$(function() {
		$('#startTime').timepicker({ 'scrollDefault': 'now', 'step':15, 'timeFormat': 'H:i', 'disableTimeRanges': bufferSlots});
		$('#endTime').timepicker({ 'scrollDefault': 'now', 'step':15, 'timeFormat': 'H:i', 'disableTimeRanges': bufferSlots});
		});
						
		$('#startTime').on('changeTime', function(e){
			
			// removes any validation error labels
			$(".startTimeSpan").css("display", "none");
			$("#startTime").removeClass("validation-error");
			
			startTime = $('#startTime').timepicker('getTime');
			
			// once the start time is selected, the endtime dropdown only has equal and greater time values 
			$('#endTime').timepicker({ 'scrollDefault': startTime, 'step':15, 'timeFormat': 'H:i', 'disableTimeRanges': bufferSlots,
			"minTime":startTime
			});
		});
		
		
		// highlights if its empty when a button is clicked
		// validates if the end time is greater than the start time
		$('#endTime').on('changeTime', function(e){
			
			// removes any validation error labels
			$(".endTimeSpan").css("display", "none");
			$("#endTime").removeClass("validation-error");
			
			startTime = $('#startTime').timepicker('getTime');
			endTime = $('#endTime').timepicker('getTime');
			
			if (endTime < startTime){
					
				alert("End time cannot be before Start time")
			}
			if (endTime.getTime() == startTime.getTime()){
					
				alert("End time cannot same as Start time")
			}
		});
		
		// capacity button event listener function
		// enables the "Book" button if a value is filled, and disables it when empty
		$('#capacity').on('keyup change', function(){
			$(".capacitySpan").css("display", "none");
			$("#capacity").removeClass("validation-error");
			if (this.value != null && this.value != ''){
			
				$('#book').prop('disabled', false);
				$('#vacancy').prop('disabled', true);
			}
			else{
				$('#book').prop('disabled', true);
				$('#vacancy').prop('disabled', false);
			}
		});
		
		// form validation function. 
		function validateForm(element){
				
				validationFlag = true
				if (element.id == 'vacancy'){
				
					if($("#startTime").val() == '' || $("#startTime").val() == null){
							
						$(".startTimeSpan").css("display", "inline");
						$("#startTime").addClass("validation-error");
						validationFlag = false;
		
					}
					
					if ($("#endTime").val() == '' || $("#endTime").val() == null){
						
							$(".endTimeSpan").css("display", "inline");
						    $("#endTime").addClass("validation-error");
							validationFlag = false;
					}
				}
				else if (element.id == "book"){
					
					if($("#startTime").val() == '' || $("#startTime").val() == null){
							
						$(".startTimeSpan").css("display", "inline");
						$("#startTime").addClass("validation-error");
						validationFlag = false;
		
					}
					
					if ($("#endTime").val() == '' || $("#endTime").val() == null){
						
							$(".endTimeSpan").css("display", "inline");
						    $("#endTime").addClass("validation-error");
							validationFlag = false;
					}
					
					if ($("#capacity").val() == '' || $("#capacity").val() == null){
						
							$(".capacitySpan").css("display", "inline");
						    $("#capacity").addClass("validation-error");
							validationFlag = false;
					}
					
				}
				return validationFlag;
		}
		
		// Check vacancy button on click event listener function
		$('#vacancy').on('click', function(e){
			 
			 // validates the form fields
			 if (!validateForm(this)){
				
				return false;
			 }
			 
			 // reads time value as date-time object
			 startTime = $('#startTime').timepicker('getTime');
			 endTime = $('#endTime').timepicker('getTime');
			 
			 // reads time value as text. e.g., 10:00
			 startTimeText = $('#startTime').val();
			 endTimeText = $('#endTime').val();
			 
			 // forming query param payload
			 myBody = {"startTime": startTimeText, "endTime":endTimeText}
			 
			 // GET method Ajax call for checking the vacant rooms for given time period
			 if(startTime != null && endTime != null) {
				$.ajax({
				type: 'GET',
				url: baseUrl + '/meeting/vacancy',
				data: myBody,
				 headers: {
				  'Content-Type': 'application/json',
				},
				crossDomain:true,
				success: function(response) {
				   console.log(response);
				   rooms = response.rooms;
				   
				   //alert(rooms.join(", ") + " room(s) are vacant");
				   
				   // Sweet alert pop-up
				   Swal.fire(
					  'Good News!',
					  rooms.join(", ") + " room(s) are vacant",
					  'success'
					)
				   resetForm();
				},
				error: function(response) {
					if (response.status == 400) {
						
						//alert(response.responseJSON.message);
						
						// Sweet alert pop-up
						Swal.fire(
						 'Oops...',
						  response.responseJSON.message,
						  'error'
						)
						resetForm();
					}
					else {
						
						//alert("Error occured. Please contact administrator");
						
						// Sweet alert pop-up
						Swal.fire(
						 'Oops...',
						  response.responseJSON.message,
						  'error'
						)
						resetForm();
					}
				}
				});
			 }
			
		});
		
		
		// resets the form and clears all the fields
		function resetForm(){
			
			$('#bookingForm')[0].reset();
			$('#book').prop('disabled', true);
			$('#vacancy').prop('disabled', false);
		}
		
		// book button on click event listener function
		$('#book').on("click", function(e){
			  
			 // validate the form fields for book
			 if (!validateForm(this)){
				
				return false;
			 }
			 
			 // reading input values
			 startTime = $('#startTime').val();
			 endTime = $('#endTime').val();
			 capacity = $('#capacity').val();
			 
			 // forming payload for booking the room
			 myBody = {"startTime" : startTime, "endTime":endTime, "capacity": capacity}
			 
			 if (capacity < 2){
				 
				alert("You can book a room for minimum of 2 members and maximum of 20 members"); 
				return false;
			 }
			 if(startTime != null && endTime != null && capacity != null && capacity > 0 && capacity < 21) {
				 
				// POST METHOD AJAX CALL FOR BOOKING A ROOM
				$.ajax({
				type: 'POST',
				url: baseUrl + '/meeting/book',
				data: JSON.stringify(myBody),
				 headers: {
				  'Content-Type': 'application/json',
				},
				crossDomain:true,
				success: function(response) {
				   console.log(response);

				   //alert(response.message);
				   
				   // Sweet alert pop-up
				   Swal.fire(
					  'Good job!',
					  response.message,
					  'success'
					)
				   resetForm();
				},
				error: function(response) {
					if (response.status == 400) {
						
						//alert(response.responseJSON.message);
						
						// Sweet alert pop-up
						Swal.fire(
						 'Oops...',
						  response.responseJSON.message,
						  'error'
						)
						resetForm();
					}
					else {
						
						//alert("Error occured. Please contact administrator");'
						
						// Sweet alert pop-up
						Swal.fire(
						 'Oops...',
						  response.responseJSON.message,
						  'error'
						)
						resetForm();
					}
				}
				});
				

		   
			 }
		});
		
});