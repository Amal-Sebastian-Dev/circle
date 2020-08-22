/*	
 * 	Password Reset
*/
// Loads the password change form async
$("#change-password").click(function () {
	console.log("change-password");
	$.ajax({
		url: '/accounts/reset/',
		type: 'get',
		dataType: 'json',
		beforeSend: function () {
			$("#modal").modal("show");
		},
		success: function (data) {
			console.log(data);
			$("#modal .modal-content").html(data.html_form);
		}
	});
});

// Submits the change password form async
$("#modal").on("submit", "#change-password-form", function () {
	var form = $(this);
	$.ajax({
		url: form.attr("action"),
		data: form.serialize(),
		type: form.attr("method"),
		dataType: 'json',
		success: function (data) {
			if (data.form_is_valid) {
				$("#messages").html(data.message);
				$("#modal").modal("hide"); 
			}
			else {
				$("#modal .modal-content").html(data.html_form);
			}
		}
	});
	return false;
});


/*
 * 	Dashboard Status wise application listing
*/
function listStatusWise(status){
	$.ajax({
		url : '/applications/applicant/status/' + status +'/',// 0 is the progress value for new applicants
		type: 'get',
		dataType: 'html',
		success: function(html) {
			$("#list-applications-statuswise").html(html);
		}
	});
};
// On Click status total card load of all applications
$("#total-count").click(function(){
	listStatusWise('All');
});
// On Click status reviewed card load of Reviewed applications
$("#reviewed-count").click(function(){
	listStatusWise('Reviewed');
});
// On Click status pending card load of Pending applications
$("#pending-count").click(function(){
	listStatusWise('Pending');
});
