$(document).ready(() => {
    try{
        let i = 0;
        let j = 0;
        let list_of_types = (document.querySelector('#list_of_types').value).split(' ');
        console.log(list_of_types)

        $('#addFields').submit((e) => {
            e.preventDefault()
            let data = $('#addFields' ).serializeArray();
            console.log(data);
            let checkbox;
            try{
                if(data[2].value == 'on') checkbox = true;
            }
            catch(e){
                checkbox = false;
            }
            let list = {
                'title': data[0].value,
                'type': data[1].value,
                'is_required': checkbox, 
            };
            list = JSON.stringify(list);

            let temp = document.createElement('input');
            temp.setAttribute('type', 'hidden');
            temp.setAttribute('name', `field_${i}`);
            temp.setAttribute('value', `${list}`);
            
            let field = document.getElementById('fields');
            field.appendChild(temp);

            let input;

            if (data[1].value == 'textarea'){
                input = document.createElement('textarea');
            }
            else{
                input = document.createElement('input');
            
            }
            input.setAttribute('class', 'form-control mb-2');
            input.setAttribute('type', `${data[1].value}`);
            input.setAttribute('placeholder', `${data[0].value} - ${data[1].value}`);
            input.setAttribute('disabled', '');

            let makets = document.getElementById('makets'); 
            makets.appendChild(input);
            i++;
            j = 0;
            $('#addFields')[0].reset();
            $("#staticBackdrop").modal('toggle');
        })

        
        $('#addValues').click(() => {
            let temp = $('#values').val();
            let input = document.createElement('input');
            input.setAttribute('type', 'hidden',);
            input.setAttribute('name', `value_${j}`,);
            input.setAttribute('value', temp);
            input.setAttribute('class', 'item_value');
            let maket = document.createElement('p');
            maket.innerHTML = temp;
            maket.set
            $('#addSelectableFiled')[0].appendChild(input);
            $('#addSelectableFiled')[0].appendChild(maket);
        });


        $('#select_type').on('change', function() {
            if(list_of_types.includes($(this).val())){
                let capacity = document.getElementById('put_selectable_data');

                
            }
        });
    }catch(e){}
});