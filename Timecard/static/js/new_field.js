<script type="text/javascript">
    $(document).ready(function () {
        var max_fields = 10; //maximum input boxes allowed
        var wrapper = $(".input_fields_wrap"); //Fields wrapper
        var add_button = $(".add_field_button"); //Add button ID

        var x = 1; //initlal text box count
        $(add_button).click(function (e) { //on add input button click
            e.preventDefault();
            if (x < max_fields) { //max input box allowed
                x++; //text box increment

                $(wrapper).append(
                    '<div><label>Labor Code:</label><select name="dropdown1">{% for site in job %}<option value="{{ site}}">{{ site }}</option>{% endfor %}</select ><label>Hrs.Worked:</label><input type="text" name="mytext[]"/><label>Total:</label><input type="text" name="mytext[]"/><a href="#" class="remove_field">Remove</a></div>'
                ); //add input box
            }
        });

        $(wrapper).on("click", ".remove_field", function (e) { //user click on remove text
            e.preventDefault(); $(this).parent('div').remove(); x--;
        })
    });


    $(document).ready(function () {
        var max_fields = 10; //maximum input boxes allowed
        var wrapper = $(".input_fields_wrap2"); //Fields wrapper
        var add_button = $(".add_field_button2"); //Add button ID

        var x = 1; //initlal text box count
        $(add_button).click(function (e) { //on add input button click
            e.preventDefault();
            if (x < max_fields) { //max input box allowed
                x++; //text box increment

                $(wrapper).append(
                    '<div><label>Machine Code:</label><select name="dropdown1">{% for site in machine %}<option value="{{ site}}">{{ site }}</option>{% endfor %}</select ><label>Hrs.Worked:</label><input type="text" name="mytext[]"/><label>Total:</label><input type="text" name="mytext[]"/><a href="#" class="remove_field">Remove</a></div>'
                ); //add input box
            }
        });

        $(wrapper).on("click", ".remove_field", function (e) { //user click on remove text
            e.preventDefault(); $(this).parent('div').remove(); x--;
        })
    });
</script>