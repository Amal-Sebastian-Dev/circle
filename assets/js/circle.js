/*	
 * 	Password Reset
*/
// Loads the password change form async
$("#change-password").click(function () {
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
// On Click status granted card load of all applications
$("#granted-count").click(function(){
	listStatusWise('Granted');
});
// On Click status reviewed card load of Reviewed applications
$("#reviewed-count").click(function(){
	listStatusWise('Reviewed');
});
// On Click status pending card load of Pending applications
$("#pending-count").click(function(){
	listStatusWise('Pending');
});

/*
 * 		Update Comment
*/
// Loads Form
$("#update-comment").click(function(){
	var id = $(this).data('id');
	$.ajax({
		url: '/applications/official/comment/'+id+'/',
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
// Submits form
$("#modal").on("submit", "#update-comment-form", function () {
	var form = $(this);
	$.ajax({
		url: form.attr("action"),
		data: form.serialize(),
		type: form.attr("method"),
		dataType: 'json',
		success: function (data) {
			if (data.form_is_valid) {
				$("#modal").modal("hide");
				$("#comment").html(data.comment);
			}
			else {
				$("#modal .modal-content").html(data.html_form);
			}
		}
	});
	return false;
});
