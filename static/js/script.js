
function addNewCategory(name) {

    document.querySelector('#categoriesContainer').insertAdjacentHTML('beforeend',
        `<li class="category">
            <span class="name">${name}</span>
            <span onclick="removeCategory(this)"class="btnRemove bold">X</span>
        </li>`)
}

function fetchCategoryArray() {
    var categories = []

    document.querySelectorAll('.category').forEach(function (e) {
        let name = e.querySelector('.name').innerHTML
        if (name == '') return;

        categories.push(name)
    })

    return categories
}

function updateCategoriesString() {
    categories = fetchCategoryArray()
    document.querySelector('input[name="categoriesString"]').value = categories.join(',')
}


function removeCategory(e) {
    e.parentElement.remove()
    updateCategoriesString()
}


function init() {
    console.log("JS works");

    document.getElementById("projectForm").addEventListener("keydown", function (e) {
        if (e.key == "Enter") {
            if (e.target.name == "categoryInput") {
                console.log("calling add");
                const catName = e.target.value;
                addNewCategory(catName)
                updateCategoriesString()
            }

            e.preventDefault();
        }
    });
}

window.onload = init;