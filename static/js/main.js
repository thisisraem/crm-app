
window.addEventListener("load", function () {
  setTimeout(function () {
    document.querySelector(".loader-container").style.display = "none";
    document.querySelector(".container").style.opacity = "1";
  }, 1000); // Adjust the timeout value as needed
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(
            cookie.substring(name.length + 1)
          );
          break;
        }
      }
    }
    return cookieValue;
  }

  var csrftoken = getCookie("csrftoken");

  
  $.ajaxSetup({
    headers: { "X-CSRFToken": csrftoken },
  });
  
  $(document).ready(function () {
    const locationSelect = $("#location");
    const storeSelect = $("#store");
    const submitButton = document.getElementById('submit-btn');
  
    function enableStoreDropdown() {
      storeSelect.prop('disabled', false);
      validateForm();
    }
  
    function disableStoreDropdown() {
      storeSelect.prop('disabled', true);
      storeSelect.val(''); // Clear the selected store value
      validateForm();
    }
  
    locationSelect.change(function () {
      var mallId = $(this).val();
      if (mallId !== "") {
        $.ajax({
          url: "/get_brands/",
          type: "GET",
          data: { mall_id: mallId },
          success: function (response) {
            storeSelect.empty();
            storeSelect.append('<option value="">Seçim--</option>');
            $.each(response.brands, function (key, value) {
              var option = $(
                '<option value="' +
                  value.id +
                  '">' +
                  value.name +
                  "</option>"
              );
              if (value.id == "{{ selected_brand }}") {
                option.attr("selected", "selected");
              }
              storeSelect.append(option);
            });
            enableStoreDropdown(); // Enable the store dropdown
          },
          error: function (xhr, status, error) {
            console.log(error);
          },
        });
      } else {
        storeSelect.empty();
        storeSelect.append('<option value="">Seçim--</option>');
        disableStoreDropdown(); // Disable the store dropdown
      }
    });
  
    function validateForm() {
      const name = document.getElementById('name').value;
      const surname = document.getElementById('surname').value;
      const gender = document.getElementById('gender').value;
      const age = document.getElementById('age').value;
      const operatorCode = document.getElementById('operator-code').value;
      const mobileNumber = document.getElementById('mobile-number').value;
      const location = document.getElementById('location').value;
      const store = document.getElementById('store').value;
  
      if (name && surname && gender && age && operatorCode && mobileNumber && location && store) {
        submitButton.disabled = false;
      } else {
        submitButton.disabled = true;
      }
    }
  
    const formInputs = document.querySelectorAll('.animated-input');
    formInputs.forEach(input => {
      input.addEventListener('input', validateForm);
    });
  
    locationSelect.change(validateForm); // Register validateForm for location change event
    storeSelect.change(validateForm); // Register validateForm for store change event
  
    disableStoreDropdown(); // Disable the store dropdown initially
    submitButton.disabled = true;
  });

  function validateInput(input) {
    input.value = input.value.replace(/[^a-zA-ZğüşıəöçĞÜŞİƏÖÇА-Яа-я]/g, '');
  }
  function validateInputNumber(input) {
    input.value = input.value.replace(/\D/g, '');
  }

  function validateInput(input) {
    input.value = input.value.replace(/[^a-zA-Z0-9@.]/g, '');
  }
 
