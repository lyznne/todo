$(document).ready(function() {
    // Handle checkbox clicks
    $('input[type="checkbox"]').change(function() {
        var taskId = $(this).attr('id').split('-')[1]; // Extract task ID from checkbox ID
        var isChecked = $(this).prop('checked');

        // Send an AJAX request to update the task's status
        $.ajax({
            url: '/update-task-status/',  // Replace with your URL
            method: 'POST',
            data: {
                task_id: taskId,
                is_checked: isChecked
            },
            success: function(response) {
                // Handle success, e.g., update UI to reflect the new status
                if (isChecked) {
                    // If checkbox is checked, set the task name text color to red
                    $('#task-name-' + taskId).css('color', 'red');
                } else {
                    // If checkbox is unchecked, reset the task name text color
                    $('#task-name-' + taskId).css('color', ''); // Empty string removes inline style
                }
            },
            error: function(error) {
                console.error(error);
            }
        });
    });
});
