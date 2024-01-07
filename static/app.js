document.addEventListener("DOMContentLoaded", function () {
    var cupcakeForm = document.getElementById("cupcakeForm");

    cupcakeForm.addEventListener("submit", function (event) {
        event.preventDefault(); 

        
        submitForm();
    });

  
   async function submitForm() {
          
         let flavor = document.getElementById("flavor").value;
         let image = document.getElementById("image").value;
         let rating = document.getElementById("rating").value;
         let size = document.getElementById("size").value;

         const response = await axios.post('/api/cupcakes/',{flavor,image,rating,size});
        console.log(response.data);
        const flavorName = response.data.cupcake.flavor;
        const  newListItem = document.createElement("li");
        const newAnchorItem = document.createElement("a")
        newAnchorItem.setAttribute("data-id",response.data.cupcake.id);
        newAnchorItem.setAttribute("href","/");
        newListItem.append(newAnchorItem);
        newAnchorItem.textContent = flavorName;
        var cupCakelist = document.getElementById("cupcakelist");
        cupCakelist.appendChild(newListItem);
        
    }
});

async function Delete(event) {
    const elementToDelete = event.target;
    const response  = await axios.delete(`/api/cupcakes/${elementToDelete.dataset.id}`)

    if (response.data.message == "delete")
    {
        location.reload();
    }
    
}

