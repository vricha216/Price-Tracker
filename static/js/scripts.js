
// forget pass

$("form[name=forget_pass_form").submit(function (e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();
  if(data.includes('otp')){
    console.log('hello');
    e.preventDefault();


    load_laoder('updating password ')
    
    $.ajax({
      url: "/user/pass/update",
      type: "POST",
      data: data,
      dataType: "json",
      success: function (resp) {
        
            load_laoder('password updated! ')            
            document.getElementsByClassName('error')[0].classList.add('error--hidden')
            close_loader()
            console.log(resp);
            window.location.href = "/user/login";
            
          },
          error: function (resp) {
            close_loader()
            $error.text('invalid otp!').removeClass("error--hidden");
            console.log(resp);
          }
        });

  }
  else{
    console.log('hello hii this is snehill');
    

      load_laoder('checking email!')

      $.ajax({
          url: "/user/check_email",
          type: "POST",
          data: data,
          dataType: "json",
          success: function (resp) {
              close_loader()
              let form_area = document.getElementById('f-form-area')
              let elem = document.createElement('input')
              elem.setAttribute('type', 'number')
              elem.setAttribute('name', 'otp')
              elem.setAttribute('class', 'field')
              elem.setAttribute('placeholder', 'Enter OTP sent on your email!')
              
              let elem1 = document.createElement('input')
              elem1.setAttribute('type', 'password')
              elem1.setAttribute('name', 'pass')
              elem1.setAttribute('class', 'field')
              elem1.setAttribute('id', 'pass_v')
              elem1.setAttribute('placeholder', 'Enter Your New Password')
              



              form_area.insertBefore(elem, form_area.children[2])
              form_area.insertBefore(elem1, form_area.children[3])

              elem = document.getElementById('check_box')
              console.log(elem);
              
              elem.classList.remove('hidden')
              console.log(resp);
                            
              document.getElementsByClassName('error')[0].classList.add('error--hidden')
              
          },
          error: function (resp) {
              close_loader()
              $error.text(resp.responseJSON.error).removeClass("error--hidden");
          }
      });
      
      e.preventDefault();
  }

  });

// signup


$("form[name=signup_form").submit(function (e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();
  
  if(data.includes('otp')){
    console.log('otp');
  
  load_laoder('signing up!')

  $.ajax({
    url: "/user/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (resp) {
      close_loader()
      window.location.href = "/";
      console.log(resp);
      console.log('hello hii this is snehill');

    },
    error: function (resp) {
        close_loader()
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });
}
else{
  alert('Please verify your email first!')
}

  e.preventDefault();
});




// signinform

$("form[name=login_form").submit(function (e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (resp) {
      window.location.href = "/";
      // console.log(resp);

    },
    error: function (resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});




// product submit form

$("form[name=product_form").submit(function (e) {


  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();
  var t_body = document.getElementById('t-body')
  var msg_not = document.getElementsByClassName('alert-not')

  load_laoder()
  $.ajax({
    url: "/user/product/add",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (res) {
      // window.location.href = "/";
      if(document.getElementById('t_h')){
        document.getElementById('t_h').classList.remove('hidden')
      }
      title = res['title']
      base_p = res['base_price']
      _id = res['_id']
      p_url = res['p_url']
      el = `<tr id="tr_${_id}">
        <td><a style="text-decoration: none; color: #c0c0c0;" href="${p_url}" target="_blank">${title}</a></td>
        <td id="p_bp_${_id}" >${base_p}</td>
        <td class="t-r">Pending</td>
        <td>
            <li class="nav-item dropdown" style="text-decoration: none; list-style: none;">
            <i class="fa fa-ellipsis-v nav-link" role="button" data-bs-toggle="dropdown" aria-hidden="true"
            style="color: #c0c0c0;" id="dot_id_${_id}"></i>
            <div id="upd_btn_id_${_id}" class="d-none">
            <button type="submit" class="btn btn-success"
                style="background-color: #0e7a0d;" id="u_p${_id}" onclick="update_product(this.id)">Update</button> 
                <i class="fa fa-1x fa-times" aria-hidden="true" id="cross_btn_${_id}" style='cursor:pointer' onclick="close_edit(this.id)"></i>
        </div>
                    
                <ul style="background-color: black;" class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <li><a class="dropdown-item t-g" 
                            style="color: #0e7a0d; font-weight: bold;" id="pe_${_id}" onclick="edit_product(this.id)"> Edit</a></li>
                    <li><a class="dropdown-item t-g" 
                            style="color: #0e7a0d; font-weight: bold;" id="pr_${_id}" onclick="del_product(this.id)">Remove</a></li>
                </ul>
            </li>

        </td>
    </tr>`

      t_body.innerHTML += el
      close_loader()
      document.getElementById('p_url').value = ""
      document.getElementById('b_price').value = ""
      msg_not[0].innerHTML = `<p class="t-g">Product added successfully!</p>`
      setTimeout(() => {
        msg_not[0].innerHTML = ""
      }, 10000);
    },
    error: function (resp) {
      close_loader()
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
      msg_not[0].innerHTML = `<p class="t-r">${resp.responseJSON.error}</p>`

    }
  });

  e.preventDefault();
})







// email verification

var v_btn = document.getElementById('v_e')
v_btn.addEventListener('click',()=>{

      let mail = document.getElementById('v_em').value
      load_laoder('sending otp...')

      url = 'email/send/otp'
      data = {'mail':mail}
      headers = { "Content-type": "application/json; charset=UTF-8" }
      fetch(url, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: headers
      })
        .then(res => res.json())
        .then(json => add_otp(json))
})



function add_otp(data){
  
  close_loader()
  if (data['status']){

    let form_area = document.getElementById('form-area')
    let elem = document.createElement('input')
    elem.setAttribute('type', 'number')
    elem.setAttribute('name', 'otp')
    elem.setAttribute('class', 'field')
    elem.setAttribute('placeholder', 'Enter OTP sent on your email!')
    
    form_area.insertBefore(elem, form_area.children[4])
    v_btn.remove()  
  }
  else{
    console.log(data);
    
    let err = document.getElementsByClassName('error--hidden')
    err[0].innerText = data['error']
    err[0].classList.remove('error--hidden')
  }

}























// edit and remove product 








var p_e = document.querySelectorAll('.pe_id')
// var p_r = document.querySelectorAll('.pr_id')
var url_el;
var price_el;
var update_btn;
var cross_btn;
var price_inhtml;
var threedot;
console.log(p_e);


function edit_product(id) {
  var id = id.slice(3,)
  price_el = document.getElementById(`p_bp_${id}`)
  update_btn = document.getElementById(`upd_btn_id_${id}`)
  threedot = document.getElementById(`dot_id_${id}`)
  price_inhtml = price_el.innerHTML
  price_el.innerHTML = `<input type="text" class="form-control" id="u_price" placeholder=${price_el.innerText} required>`
  threedot.classList.add('d-none')
  update_btn.classList.remove('d-none')
}

function close_edit(id) {
  console.log(price_inhtml, price_el);

  cross_btn = document.getElementById(`cross_btn_${id}`)
  price_el.innerHTML = price_inhtml
  threedot.classList.remove('d-none')
  update_btn.classList.add('d-none')
}


function update_product(id) {

  last_price = price_inhtml
  curr_price = document.getElementById('u_price').value

  if (last_price == curr_price) {
    console.log('do nothing!');

  }
  else {


    let data = { 'price': curr_price, 'p_id': id }
    url = '/user/product/edit'
    headers = { "Content-type": "application/json; charset=UTF-8" }
    load_laoder()
    fetch(url, {
      method: 'POST',
      body: JSON.stringify(data),
      headers: headers
    })
      .then(res => res.json())
      .then(json => data_updated(json))
      .catch(err => console.log(err, "dwdw"))


    price_el.innerHTML = curr_price
    console.log('make update');

  }

  update_btn.classList.add('d-none')
  threedot.classList.remove('d-none')

}



function del_product(id) {
  let data = { 'p_id': id }
  url = '/user/product/del'
  headers = { "Content-type": "application/json; charset=UTF-8" }
  load_laoder()
  fetch(url, {
    method: 'POST',
    body: JSON.stringify(data),
    headers: headers
  })
    .then(res => res.json())
    .then(json => data_deleted(json, id)
    )
    .catch(err => console.log(err))


}


function data_updated(data) {
  close_loader()
  console.log(data);
}

function data_deleted(data, id) {
  close_loader()
  id = id.slice(3,)
  t_id = "tr_" + id
  elem = document.getElementById(t_id)
  elem.remove()
  console.log(data, id);

}

function load_laoder(msg='not declared yet!') {
  document.getElementById('noti-msg').innerText = msg
  loader = document.getElementById('loader')
  loader.classList.remove('hidden')
}

function close_loader() {
  loader = document.getElementById('loader')
  loader.classList.add('hidden')
}



function show_pass(elem){
  console.log(elem.checked);
  let pass_v = document.getElementById('pass_v')

  if(elem.checked){
    pass_v.type="text"
    
  }
  else{
    pass_v.type="password"
  }
  
}