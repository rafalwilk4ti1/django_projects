var form_fields = document.getElementsByTagName('input')
		form_fields[1].placeholder='Name..';
		form_fields[2].placeholder='Surname..';
		form_fields[3].placeholder='Email..';
		form_fields[4].placeholder='Phone cell...';

		for (var field in form_fields){
			form_fields[field].className += ' form-control'
		}
