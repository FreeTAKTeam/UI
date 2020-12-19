	<script>
		var checkbox = document.querySelector("input[id=OnOffSwitch]");
		var OnJson = {"CoTService": {"IP": "0.0.0.0", "PORT": "15777", "STATUS": "start"}, "DataPackageService": {"IP": "192.168.2.74", "PORT": "8080", "STATUS":"start"}}
		checkbox.addEventListener( 'change', function() {
		    if(this.checked) {
		        const url='http://192.168.2.74/All';
				const Http = new XMLHttpRequest();
				Http.open("POST", url);
				Http.setRequestHeader("Content-Type", "application/json");
				console.log(OnJson);
				Http.send(OnJson);
				Http.onreadystatechange = (e) => {
					console.log(Http.responseText);
				}
		    } else {
		        // pass
		    }
		});
	</script>