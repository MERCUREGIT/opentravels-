function join_trip() {
    item = document.getElementById('trip_list_item').innerHTML;
    window.console.log(item);
}



// implement onclick event to display trip posting form
function display_form() {

            form_display = document.getElementById('trip_post_form');
            
            if (form_display.style.display == "none") {
                form = document.getElementById('trip_post_form').style.display = "block";
                
            }
            else
            {
                form = document.getElementById('trip_post_form').style.display = "none";
            }
        }