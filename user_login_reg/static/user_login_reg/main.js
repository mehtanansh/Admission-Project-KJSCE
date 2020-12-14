var listOfDocuments = []
let noOfActivities = 1;
		function removeRow(rowID){
			let temp = document.getElementById(rowID)
				if(!(temp == null)){
					console.log("OK")
					setTimeout(function(){
						temp.parentNode.removeChild(temp)
						let index = listOfDocuments.indexOf(rowID)
						listOfDocuments.splice(index,1)
					},0)	
				}
		}

		function createRows(){
			var cet = document.getElementById('cet_check')
			var jeem = document.getElementById('jeem_check')
			var jeea = document.getElementById('jeea_check')
			var pwd =  document.getElementById('pwd_check')

			if(cet.checked == true){
				let index = listOfDocuments.indexOf("CETMarksheet")
				if(index == -1)
					listOfDocuments.push("CETMarksheet")
			}else{
				removeRow("CETMarksheet")
			}
			if(jeem.checked == true){
				let index = listOfDocuments.indexOf("JEEMainsMarksheet")
				if(index == -1)
					listOfDocuments.push("JEEMainsMarksheet")
			}else{
				removeRow("JEEMainsMarksheet")
			}
			if(jeea.checked == true){
				let index = listOfDocuments.indexOf("JEEAdvanceMarksheet")
				if(index == -1)
					listOfDocuments.push("JEEAdvanceMarksheet")
			}else{
				removeRow("JEEAdvanceMarksheet")
			}
		
			
			let table = document.getElementById('uploadTable')
			for(let i = 0 ; i < listOfDocuments.length ; i++){
				let temp = document.getElementById(listOfDocuments[i])
				if(!(temp == null)){
					continue	
                }
                // <div class="custom-file mb-3">
                //     <input type="file" name="SSCMarksheet" class="custom-file-input" id="customFile" valu = "{{ candidate.ssc_result }}">
                //     <label class="custom-file-label" for="customFile">SSC Marksheet</label>
                // </div>
                let div = document.createElement('div')
                div.setAttribute("class","custom-file mb-3")
                div.setAttribute("id",listOfDocuments[i])
				let input = document.createElement('input')
				input.setAttribute("type","file")
                input.setAttribute("name",listOfDocuments[i])
                input.setAttribute("class","custom-file-input")
                input.setAttribute("change","validateFiles(event)")
                let label = document.createElement('label')
                label.setAttribute("class","custom-file-label")
				label.innerHTML = listOfDocuments[i]
                div.appendChild(input)
                div.appendChild(label)
				table.appendChild(div)
			}
		}


		function upload_photo(event){
			var photoUpload = document.getElementById('photo_input')
			photoUpload.click();
		}

		function showStudentImage(event){
			var photoUpload = document.getElementById('photo_input')
			var img = document.getElementById('photo')
			if(photoUpload.files.length == 1){
				var reader = new FileReader();
				reader.readAsDataURL(photoUpload.files[0]);

				reader.onload = function(e){
						img.setAttribute("src",e.target.result)
				}
			}
		}

		function displayPersonal(event){
			var personal_details = document.getElementById('personal_details')
			var academic_details = document.getElementById('academic_details')
            var upload_files = document.getElementById('upload_files')
            var eca = document.getElementById('eca')
            // document.getElementById('submit').style.display = "none"
			personal_details.style.display = "flex"
			academic_details.style.display = "none"
			upload_files.style.display = "none"
			eca.style.display = "none"
			preference_details.style.display = "none"
		}
		function displayAcademic(event){
			var personal_details = document.getElementById('personal_details')
			var academic_details = document.getElementById('academic_details')
            var upload_files = document.getElementById('upload_files')
			var eca = document.getElementById('eca')
			var preference_details = document.getElementById('preference_details')
            //document.getElementById('submit').style.display = "none"
			personal_details.style.display = "none"
			academic_details.style.display = "flex"
			eca.style.display = "none"
			preference_details.style.display = "none"
			upload_files.style.display = "none"
			// alert("ok")
		}
		function displayECA(event){
			var personal_details = document.getElementById('personal_details')
			var academic_details = document.getElementById('academic_details')
			var upload_files = document.getElementById('upload_files')
			var preference_details = document.getElementById('preference_details')
            // document.getElementById('submit').style.display = "none"
            var eca = document.getElementById('eca')
			personal_details.style.display = "none"
			academic_details.style.display = "none"
			upload_files.style.display = "none"
			eca.style.display = "flex"
			preference_details.style.display = "none"
			
		}
		function displayUpload(event){
			var personal_details = document.getElementById('personal_details')
			var academic_details = document.getElementById('academic_details')
			var upload_files = document.getElementById('upload_files')
			var eca = document.getElementById('eca')
			var preference_details = document.getElementById('preference_details')
			personal_details.style.display = "none"
			academic_details.style.display = "none"
            upload_files.style.display = "flex"
			eca.style.display = "none"
			preference_details.style.display = "none"
            // document.getElementById('submit').style.display = "flex"
			createRows()
		}
		function displayPref(event){
			var personal_details = document.getElementById('personal_details')
			var academic_details = document.getElementById('academic_details')
			var upload_files = document.getElementById('upload_files')
			var preference_details = document.getElementById('preference_details')
            var eca = document.getElementById('eca')
			personal_details.style.display = "none"
			academic_details.style.display = "none"
            upload_files.style.display = "none"
            eca.style.display = "none"
            preference_details.style.display = "flex"
		}
		function createCETInput(){
			var cet = document.getElementById('cet_check')
			if(cet.checked == true){
				var temp = document.getElementById('cet_input')
				if(temp == null){
                    var cetWDiv = document.createElement('div')
                    cetWDiv.setAttribute("class","col-md-12")
                    var cet_label = document.createElement('label')
					cet_label.innerHTML = 'CET Total Marks'
					var cet_div = document.createElement('div')
					var cet_input = document.createElement('input')
					cet_input.setAttribute("type","number")
					cet_input.setAttribute("id","cet_input")
					cet_input.setAttribute("class","form-control form-control-lg")
					cet_input.setAttribute("name","cetmarks")
					cet_input.placeholder="CET Marks"
                    cet_div.setAttribute("id","cet_div")
                    cet_div.setAttribute("class","form-group")
                    cet_div.appendChild(cet_label)
                    cet_div.appendChild(cet_input)
                    cetWDiv.appendChild(cet_div)
					var wrapper = document.getElementById("cetWrapper")
					wrapper.appendChild(cetWDiv)
					createCETEach()
				}	
			}else{
				var cet_div = document.getElementById("cet_div")
				if(cet_div)
					cet_div.parentNode.removeChild(cet_div)
					removeCETEach()
			}
		}

		function createSETInput(){
			var cet = document.getElementById('set_check')
			if(cet.checked == true){
				var temp = document.getElementById('set_input')
				if(temp == null){
                    var cetWDiv = document.createElement('div')
                    
					var cet_div = document.createElement('div')
					var cet_label = document.createElement('label')
					cet_label.innerHTML = 'SUVCET Marks'
					var cet_input = document.createElement('input')
					cet_input.setAttribute("type","number")
					cet_input.setAttribute("id","set_input")
					cet_input.setAttribute("class","form-control form-control-lg")
					cet_input.setAttribute("name","setmarks")
					cet_input.placeholder="SUVCET"
                    cet_div.setAttribute("id","set_div")
                    cet_div.setAttribute("class","form-group")
                    cet_div.appendChild(cet_label)
                    cet_div.appendChild(cet_input)
                    cetWDiv.appendChild(cet_div)
					var wrapper = document.getElementById("setWrapper")
					wrapper.appendChild(cetWDiv)
				}	
			}else{
				var cet_div = document.getElementById("set_div")
				if(cet_div)
					cet_div.parentNode.removeChild(cet_div)
					// removeCETEach()
			}
		}

		function createJEEMInput(){
			var cet = document.getElementById('jeem_check')
			
			if(cet.checked == true){
				
				var temp = document.getElementById('jeem_input')
				if(temp == null){
                    console.log("OK")
                    var cetWDiv = document.createElement('div')
                    cetWDiv.setAttribute("class","col-md-6")
					var cet_div = document.createElement('div')
					
					var cet_label = document.createElement('label')
					cet_label.innerHTML = 'JEE Mains Marks' 
					var cet_input = document.createElement('input')
					cet_input.setAttribute("type","number")
					cet_input.setAttribute("id","jeem_input")
					cet_input.setAttribute("class","form-control form-control-lg")
					cet_input.setAttribute("name","JEEMainsMarks")
					cet_input.placeholder="JEE Mains Marks"
                    cet_div.setAttribute("id","jeem_div")
                    cet_div.setAttribute("class","form-group")
					
					cet_div.appendChild(cet_label)
                    cet_div.appendChild(cet_input)
                    cetWDiv.appendChild(cet_div)
					var wrapper = document.getElementById("jeeWrapper")
					wrapper.appendChild(cetWDiv)
				}	
			}else{
				
				var cet_div = document.getElementById("jeem_div")
				if(cet_div);
					cet_div.parentNode.removeChild(cet_div)
					
			}
		}
		function createCETEach(){

            // var mainDiv = document.createElement('div')
            // mainDiv.setAttribute("id","mainDiv")
            // mainDiv.setAttribute("class","row")


            var cetWDivp = document.createElement('div')
            cetWDivp.setAttribute("class","col-md-4")
            var cet_divp = document.createElement('div')
            var cet_label = document.createElement('label')
            var cet_small = document.createElement('small')
			cet_small.innerHTML = 'CET Physics Marks'
			var cet_inputp = document.createElement('input')
			cet_inputp.setAttribute("type","number")
			cet_inputp.setAttribute("id","cet_inputp")
			cet_inputp.setAttribute("class","form-control form-control-lg")
			cet_inputp.setAttribute("name","CETPhysicsMarks")			
			cet_inputp.placeholder="CET Physics"
			// cet_divp.setAttribute("id","cete_div")
            cet_divp.setAttribute("class","form-group")
			cet_label.appendChild(cet_small)
            cet_divp.appendChild(cet_label)
			cet_divp.appendChild(cet_inputp)
            cetWDivp.appendChild(cet_divp)
            // mainDiv.appendChild(cetWDivp)

			
			// var cet_inputm = document.createElement('input')
			// cet_inputm.setAttribute("type","number")
			// cet_inputm.setAttribute("id","cet_inputm")
			// cet_inputm.setAttribute("class","marks")
			// cet_inputm.setAttribute("name","CETMathematicsMarks")
			// cet_inputm.placeholderL="CET Maths"
			// cet_div.appendChild(cet_labelm)
			// cet_div.appendChild(cet_inputm)
			// cet_div.appendChild(document.createElement('br'))
			// var cet_labelc = document.createElement('label')
            
            var cetWDivm = document.createElement('div')
            cetWDivm.setAttribute("class","col-md-4")
            var cet_divm = document.createElement('div')
            var cet_label = document.createElement('label')
            var cet_small = document.createElement('small')
			cet_small.innerHTML = 'CET Maths Marks'
			var cet_inputm = document.createElement('input')
			cet_inputm.setAttribute("type","number")
			cet_inputm.setAttribute("id","cet_inputm")
			cet_inputm.setAttribute("class","form-control form-control-lg")
			cet_inputm.setAttribute("name","CETMathematicsMarks")			
			cet_inputm.placeholder="CET Mathematics"
			// cet_divm.setAttribute("id","cete_div")
            cet_divm.setAttribute("class","form-group")
            cet_label.appendChild(cet_small)
            cet_divm.appendChild(cet_label)
			cet_divm.appendChild(cet_inputm)
           	cetWDivm.appendChild(cet_divm)
            // mainDiv.appendChild(cetWDivm)


			// cet_inputc.setAttribute("type","number")
			// cet_inputc.setAttribute("id","cet_inputp")
			// cet_inputc.setAttribute("class","marks")
			// cet_inputc.setAttribute("name","CETChemistryMarks")
			// cet_inputc.placeholderL="CET Chemistry"
			// cet_div.appendChild(cet_labelc)
			// cet_div.appendChild(cet_inputc)
			// cet_div.appendChild(document.createElement('br'))
			// var wrapper = document.getElementById("academic_details")
			// wrapper = wrapper.children[0]
            // wrapper.appendChild(cet_div)
            


            var cetWDivc = document.createElement('div')
            cetWDivc.setAttribute("class","col-md-4")
            var cet_divc = document.createElement('div')
            var cet_label = document.createElement('label')
            var cet_small = document.createElement('small')
			cet_small.innerHTML = 'CET Chemistry Marks'
			var cet_inputc = document.createElement('input')
			cet_inputc.setAttribute("type","number")
			cet_inputc.setAttribute("id","cet_inputc")
			cet_inputc.setAttribute("class","form-control form-control-lg")
			cet_inputc.setAttribute("name","CETChemistryMarks")			
			cet_inputc.placeholder="CET Chemistry"
			// cet_divc.setAttribute("id","cete_div")
            cet_divc.setAttribute("class","form-group")
            cet_label.appendChild(cet_small)
            cet_divc.appendChild(cet_label)
			cet_divc.appendChild(cet_inputc)
            cetWDivc.appendChild(cet_divc)
            // mainDiv.appendChild(cetWDivc)

            document.getElementById('cetEachWrapper').appendChild(cetWDivm)
            document.getElementById('cetEachWrapper').appendChild(cetWDivp)
            document.getElementById('cetEachWrapper').appendChild(cetWDivc)

		}
		function removeCETEach(){
			var d = document.getElementById('cetEachWrapper')
			if(d)
				d.removeChild(d.childNodes[0])
				d.removeChild(d.childNodes[0])
				d.removeChild(d.childNodes[0])
				d.removeChild(d.childNodes[0])
		}
		function createJEEAInput(){
			var cet = document.getElementById('jeea_check')
			if(cet.checked == true){
				var temp = document.getElementById('jeea_input')
				if(temp == null){
				
                    var cetWDiv = document.createElement('div')
                    cetWDiv.setAttribute("class","col-md-6")
					var cet_div = document.createElement('div')
					var cet_label = document.createElement('label')
					cet_label.innerHTML = 'JEE advance Marks'
					var cet_input = document.createElement('input')
					cet_input.setAttribute("type","number")
					cet_input.setAttribute("id","jeea_input")
					cet_input.setAttribute("class","form-control form-control-lg")
					cet_input.setAttribute("name","JEEAdvanceMarks")
					cet_input.placeholder="JEE advance Marks"
                    cet_div.setAttribute("id","jeea_div")
                    cet_div.setAttribute("class","form-group")
                    cet_div.appendChild(cet_label)
                    cet_div.appendChild(cet_input)
                    cetWDiv.appendChild(cet_div)
					var wrapper = document.getElementById("jeeWrapper")
					wrapper.appendChild(cetWDiv)


				}	
			}else{
				var cet_div = document.getElementById("jeea_div")
				if(cet_div)
				cet_div.parentNode.removeChild(cet_div)
				// alert("working?")
			}
        }
        

function validate(){
    var list  = document.getElementsByTagName('input')
    let text_list = []
    let  year_list = []
    let date
    let email_list = []
	let number_list = []
    let file_list = []
    let alerted = 0
    for(let i = 0 ; i < list.length ; i++){
        if(list[i].getAttribute("type") ==  "text"){
            if(list[i].getAttribute('name') == "SSCPassingYear" || list[i].getAttribute('name') == "HSCPassingYear")
                year_list.push(list[i])
            else
                text_list.push(list[i])
    
        }else if(list[i].getAttribute("type") ==  "date"){
            date = list[i]
        }
        else if(list[i].getAttribute("type") == "email"){
            email_list.push(list[i])
        }else if(list[i].getAttribute("type") == "number"){
			number_list.push(list[i])	
		}else if(list[i].getAttribute("type") == "file"){
			file_list.push(list[i])
			console.log(list[i].getAttribute('name'))
		}
    }					
	

    char_regex = /[a-zA-Z]+/
    for(let i = 0 ; i < text_list.length ; i++){
        if(text_list[i].value == ""){
            alert(text_list[i].getAttribute('name') + " cannot be empty")
            return;
        }else if((!char_regex.test(text_list[i].value))){
            alert(text_list[i].getAttribute('name') + " cannot contain numbers")
            return;
        }
    }

    year_regez = /[0-9]{4}/
    for(let i = 0 ; i < year_list.length ; i++){
        let d = new Date()
        if(text_list[i].value == ""){
            alert(text_list[i].getAttribute('name') + " cannot be empty")
            return;
        }else if((!year_regex.test(year_list[i].value))){
            alert("Enter valid year in " + text_list[i].getAttribute('name'))
            return;
        }else
         if(year_list[i].value > d.getFullYear()){    
			alert("Enter valid year in " + year_list[i].getAttribute('name'))
			return
        }
    }
    
    if(date.value>getDefaultDate()){
		alert("Enter valid DOB");
		return
    }

    var email_regex = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/
    for(let  i = 0 ; i < email_list.length ; i++){
        if(email_list[i].value == ""){
            alert("Enter emial id in " + email_list[i].getAttribute('name')) 
            return;
        }
        if(!(email_regex.test(email_list[i].value))){
            alert("Enter valid email id in " + email_list[i].getAttribute('name'))
            return;
        }
    }


    var gender_list = document.getElementsByName('gender')
    let flag = 0
    for(let i = 0 ;i < gender_list.length ; i++){
        if(gender_list[i].checked == true){
            flag = 1
        }
        if(flag == 0){
            alert("Select one of the genders")
            return;
        }
    }

    let cet_check = document.getElementById('cet_check')
    let jeea_check = document.getElementById('jeea_check')
    let jeem_check = document.getElementById('jeem_check')
    if(jeea_check.checked == true)
    {   
        if(jeem_check.checked == false){
			alert("You should appear for JEE Mains for JEE advance")
			return
        }
    }else if(cet_check.checked == false && jeea_check.checked == false && jeem_check.checked == false){
		alert("Select atleast one of the Examinations")
		return
    }
		let pincode_regex = /^[0-9]{6}$/
		let number_regex = /^\d{10}$/
		for(let i = 0 ; i< number_list.length ; i++){
		 	let name  = number_list[i].getAttribute("name")
			if(name == "Pincode"){
				if(number_list[i].value == ""){
					alert("Enter  Pincode")
					return
				}
				else if(!(pincode_regex.test(number_list[i].value))){
					alert("Enter valid Pincode")
					return
				} 
			}else if(name == "parentGuardianMobile" || name == "mobile"){
				if(number_list[i].value == ""){
					alert("Enter  mobile number in " + number_list[i].getAttribute("name"))
					return
				}
				else if(!(number_regex.test(number_list[i].value))){
					alert("Enter valid mobile number in " + number_list[i].getAttribute("name"))
					return
				}
			}else if(name == "SSCPercentage" || name== "HSCPercentage"){
					if(number_list[i].value == ""){
						alert("Enter percentage in " + number_list[i].name)
						return
					}
					else if(!(number_list[i].value >= 0 &&  number_list[i].value <= 100)){
						alert("Enter valid percentage in " + number_list[i].name)
						return
					}
			}
			else{
				if(name == "CETMarks"){
					console.log("OK")
					if(!(number_list[i].value >= 0 && number_list[i].value <= 200) || number_list[i].value == ""){
						alert("Enter valid CET marks")
						return
					}
				}else if(name == "JEEMainsMarks"){
					if(!(number_list[i].value >= 0 && number_list[i].value <= 300) || number_list[i].value == ""){
						alert("Enter valid JEE mains marks")
						return
					}
				}else if(name == "JEEAdvanceMarks"){
					if(number_list[i].value == ""){
						alert("Enter valid JEE advance marks")
						return
					}
				}else if ( name == "HSCPhysicsMarks" ||  name == "HSCChemistry Marks" ||  name == "HSCMathematicsMarks"){
					if(!(number_list[i].value >= 0 && number_list[i].value <= 100) || number_list[i].value == ""){
						alert("Enter valid " + name)
						return
					}
				}
			}
		 }

	for(let  i = 0 ; i< file_list.length ; i++){
		console.log("OK")
		if(file_list[i].files.length == 0){
			alert("Upload " + file_list[i].getAttribute("name"))
			return;									
		}
	}  
		
	 }



function getDefaultDate(){

    var now = new Date();
    var day = ("0" + now.getDate()).slice(-2);
    var month = ("0" + (now.getMonth() + 1)).slice(-2);
    var today = (day)+"-"+(month)+"-"+now.getFullYear();
    console.log(today)
    return today;
}

function init(){
    var list  = document.getElementsByTagName('input')
    let file_list = []
	
    let alerted = 0
    for(let i = 0 ; i < list.length ; i++){
         if(list[i].getAttribute("type") == "file"){
			file_list.push(list[i])
		}
    }	
    for(let i = 0 ; i < file_list.length ; i++){
        if(file_list[i].getAttribute("name") != "candidatePhoto" ){
            file_list[i].addEventListener("change",function(event){
                validateFiles(event)
            })
            console.log(file_list[i].getAttribute("name"))
        }
    }
}

function validateFiles(event){			
  
    name = event.target.name
    let el
    if(event){
         el = event.target
    if(el.files.length > 0){
        console.log(event.target.files)
        let size_kb = el.files[0].size / 1024
        let mime = el.files[0].type
		
		if(name == "Signature" || name == "candidatePhoto"){
			if(mime == "image/jpeg"){
				if(size_kb>500){
					alert("File size cannot be more then 500kb")
					el.value = ""
					return
				}
			}else{
				alert("Only JPEG files are allowed")
				el.value = ""    
				return
			}
		}else{
			if(mime == "image/jpeg" || mime == "application/pdf"){
				if(size_kb>500){
					alert("File size cannot be more then 500kb")
					el.value = ""
					return
				}
			}else{
				alert("Only JPEG and PDF files are allowed")
				el.value = ""    
				return
			}
			
		}
		}
		
        
	}
}

function displayName(){
    console.log("OK")
    let iname = document.getElementById('fName')
    let name = document.getElementById("student_name")
    name.innerHTML = "Name: " + iname.value
}
function displayFields(event){
	if(event.target.value == "NRI"){
		document.getElementById('secondlist').style.display = "none"
		document.getElementById('listBox').style.display = "none"
		document.getElementById('state').style.display = "block"
		document.getElementById('district').style.display = "block"
		// document.getElementById('state').style.position = document.getElementById('secondlist').style.position
		// document.getElementById('district').style.position = document.getElementById('listBox').style.position
	}else{
		document.getElementById('secondlist').style.display = "block"
		document.getElementById('listBox').style.display = "block"
		document.getElementById('state').style.display = "none"
		document.getElementById('district').style.display = "none"
	}
}

function addMoreActivities(){
	
	if(noOfActivities == 10){
		alert("Number of activities cannot be more then 10.")
		return
	}

	let e = document.getElementById('ecaContainer')
	let list = e.childNodes
	let list2 = Array.from(list)
	var res = list2.filter(ele =>{
		let cl = ele.className
		return cl == 'row'
	});

	// <div class="row">
	// <div class="col-md-6">
	// 	<div class="form-group">
	// 		<label>Activity Name</label>
	// 		<input type="text" class="form-control form-control-lg" name="DEMO" placeholder="Name of the Activity">	
	// 	</div>	
	// </div>
	// <div class="col-md-6">
	// 	<div class="form-group">
	// 		<label>Participation Year</label>
	// 		<input type="text" class="form-control form-control-lg" name="DEMO" placeholder="Year of the Participation">	
	// 	</div>	
	// </div>
	// <div class="col-md-12">
	// 	<label>Certificates</label>
	// 	<input type="file" class="form-control-file border" name="DEMO" placeholder="Year of the Participation">	
	// </div>
	// </div>

	var mainDiv = document.createElement('div')
	mainDiv.setAttribute('class','row')

	var leftDivWrapper = document.createElement('div')
	leftDivWrapper.setAttribute('class','col-md-6')
	var leftDiv = document.createElement('div')
	leftDiv.setAttribute('class','form-group')
	var label_l = document.createElement('label')
	label_l.innerHTML = "Activity Name"
	var input_l = document.createElement('input')
	input_l.setAttribute('type','text')
	input_l.setAttribute('class','form-control form-control-lg')
	input_l.setAttribute('placeholder','Name of the Activity')
	leftDiv.appendChild(label_l)
	leftDiv.appendChild(input_l)
	leftDivWrapper.appendChild(leftDiv)


	var rightDivWrapper = document.createElement('div')
	rightDivWrapper.setAttribute('class','col-md-6')
	var rightDiv = document.createElement('div')
	rightDiv.setAttribute('class','form-group')
	var label_l = document.createElement('label')
	label_l.innerHTML = "Participation year"
	var input_l = document.createElement('input')
	input_l.setAttribute('type','text')
	input_l.setAttribute('class','form-control form-control-lg')
	input_l.setAttribute('placeholder','Year of the Participation')
	rightDiv.appendChild(label_l)
	rightDiv.appendChild(input_l)
	rightDivWrapper.appendChild(rightDiv)



	
	var midDivWrapper = document.createElement('div')
	midDivWrapper.setAttribute('class','col-md-12')
	var midDiv = document.createElement('div')
	midDiv.setAttribute('class','form-group')
	var label_l = document.createElement('label')
	label_l.innerHTML = "Certificates"
	var input_l = document.createElement('input')
	input_l.setAttribute('type','file')
	input_l.setAttribute('class','form-control-file border')
	input_l.setAttribute('placeholder','Year of the Participation')
	midDiv.appendChild(label_l)
	midDiv.appendChild(input_l)
	midDivWrapper.appendChild(midDiv)



	mainDiv.appendChild(leftDivWrapper)
	mainDiv.appendChild(rightDivWrapper)
	mainDiv.appendChild(midDivWrapper)


	e.insertBefore(mainDiv,res[res.length - 2])
	noOfActivities++;

}

function removeLastActivity(){

	if(noOfActivities == 1){
		alert("Number of activities cannot be less then 1.")
		return
	}

	let e = document.getElementById('ecaContainer')
	let list = e.childNodes
	let list2 = Array.from(list)
	var res = list2.filter(ele =>{
		let cl = ele.className
		return cl == 'row'
	});
	if(res.length > 2)	
	res[res.length - 2].parentNode.removeChild(res[res.length - 3])
	noOfActivities--;
}

function getPreference(){
	let main = document.getElementById('example2-right')
	let res = document.getElementById('preferenceResults')
	let span = document.createElement('span')
	let list = main.childNodes
	for(let i = 0 ; i < list.length ; i++){
		span.innerHTML += (i+1) + " " + list[i].innerHTML + "\n"
	}
	
	if(span.innerHTML == ""){
		span.innerHTML = ""
		return
	}
	else{
		if(res.childNodes.length > 0){
			while (res.firstChild) {
				res.removeChild(res.firstChild);
			  }
		}
		res.appendChild(span)
	}	
	
}