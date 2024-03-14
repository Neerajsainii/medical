// let names = [
//     "Muscle aches", "Shortness of breath", "New loss of taste or smell", 
//     "Chest pain", "Confusion (especially in older adults)", "Chest tightness",
//     "Wheezing", "Coughing", "Chronic cough", "Production of mucus (sputum)",
//     "Chest discomfort", "Hoarseness", "Unintended weight loss",
//     "Chest pain or discomfort (angina)", "Heart attack (sudden, severe chest pain, often radiating to the left arm or shoulder, sweating, nausea, vomiting, dizziness, shortness of breath)",
//     "Swelling (edema) in legs, ankles, and feet", "Rapid or irregular heartbeat",
//     "Increased need to urinate at night", "Sudden weight gain", "Nosebleeds",
//     "Flushing", "Dizziness", "Visual changes", "Frequent urination",
//     "Increased thirst", "Extreme hunger", "Unexplained weight loss", "Irritability",
//     "Blurry vision", "Slow-healing sores", "Frequent infections", "Weight gain",
//     "Constipation", "Dry skin", "Cold intolerance", "Joint and muscle pain",
//     "Depression", "Slowed heart rate", "Rapid heartbeat", "Irregular heartbeat (arrhythmia)",
//     "Increased appetite", "Nervousness, anxiety, and irritability", "Sweating",
//     "Tremors", "Changes in menstrual patterns", "Digestive symptoms (diarrhea, bloating, gas, abdominal pain)",
//     "Weight loss", "Anemia", "Osteoporosis", "Skin rash (dermatitis herpetiformis)",
//     "Abdominal pain and cramping", "Blood in your stool", "Mouth sores",
//     "Reduced appetite and weight loss", "Perianal disease (pain or drainage near the anus)",
//     "Diarrhea (with blood or pus)", "Rectal pain", "Rectal bleeding", "Urgency to defecate",
//     "Abdominal pain or cramping", "Feeling full after eating small amounts of food",
//     "Heartburn", "Nausea", "Vomiting", "Dark or black stool", "Abdominal pain (usually in the upper abdomen)",
//     "Feeling full after eating small amounts of food", "Heartburn", "Nausea", "Vomiting", "Dark or black stool",
//     "Abdominal pain (usually on the left side)", "Fever", "Nausea and vomiting", "Constipation", "Diarrhea",
//     "Rectal bleeding", "Severe pain in the side and back, below the ribs",
//     "Pain that radiates to the lower abdomen and groin", "Painful urination",
//     "Pink, red, or brown urine", "Cloudy or foul-smelling urine", "Persistent need to urinate",
//     "Urinating more often than usual", "Strong, persistent urge to urinate", "Burning"];

  //Sort names in ascending order
  let sortedNames = names.sort();
  
  //reference
  let input = document.getElementById("input");
  
  //Execute function on keyup
  input.addEventListener("keyup", (e) => {
    //loop through above array
    //Initially remove all elements ( so if user erases a letter or adds new letter then clean previous outputs)
    removeElements();
    for (let i of sortedNames) {
      //convert input to lowercase and compare with each string
  
      if (
        i.toLowerCase().startsWith(input.value.toLowerCase()) &&
        input.value != ""
      ) {
        //create li element
        let listItem = document.createElement("li");
        //One common class name
        listItem.classList.add("list-items");
        listItem.style.cursor = "pointer";
        listItem.setAttribute("onclick", "displayNames('" + i + "')");
        //Display matched part in bold
        let word = "<b>" + i.substr(0, input.value.length) + "</b>";
        word += i.substr(input.value.length);
        //display the value in array
        listItem.innerHTML = word;
        document.querySelector(".list").appendChild(listItem);
      }
    }
  });
  function displayNames(value) {
    input.value = value;
    removeElements();
  }
  function removeElements() {
    //clear all the item
    let items = document.querySelectorAll(".list-items");
    items.forEach((item) => {
      item.remove();
    });
  }