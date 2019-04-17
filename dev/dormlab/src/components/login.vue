<template>
<!-- Login -->
    <div class="container">
        <div class="row mt-5 pt-5">
            <div class="col-md-3"></div>
            <div class="col-md-6 bg-white p-5" style="border-radius: .3em;box-shadow: 0px 0px 25px rgba(0, 0, 0, 0.315)">
                <div class="d-flex justify-content-center">
                    <!-- <img src="https://i.imgur.com/dtLbFJe.jpg" class="mx-auto mb-4"> -->
                    <h1 class="mx-auto mb-4">DormLab | Login</h1>
                </div>
                <!--<h3 class="text-center mb-3">เข้าสู่ระบบ</h3>-->
                <form>
                    <div class="form-group">
                        <label for="username"><i class="fas fa-user"></i> ชื่อผู้ใช้งาน</label>
                        <input type="text" class="form-control" id="username">
                    </div>
                    <div class="form-group">
                        <label for="password"><i class="fas fa-lock"></i> รหัสผ่าน</label>
                        <input type="password" class="form-control" id="password">
                    </div>
                    <!-- <button type="reset" class="btn btn-danger float-right"><i class="fas fa-trash-alt"></i> ล้าง</button> -->
                    <button type="submit" class="btn btn-primary float-right mr-1"><i class="fas fa-sign-in-alt"></i> เข้าสู่ระบบ</button>
                    <br><br><hr>
                    <span class="float-right">หากไม่มีบัญชี กรุณา <a href="register.html" class="btn btn-warning"><i class="fas fa-user-plus"></i> สมัครสมาชิกใหม่</a></span>
                </form>
            </div>
            <div class="col-md-3"></div>
        </div>
    </div> 
    <!-- / Login -->
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
*{
  font-family: 'Sarabun', sans-serif;
}
body{
  background: #1a535c;
}
h1{
  font-family: 'Timmana', sans-serif;
}
</style>
