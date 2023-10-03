<!-- Login.vue -->
<template>
    <div>
        <hi>Login</hi>
        <br>
        <input
          type="username"
          name="username"
          v-model="username"
          placeholder="Username"/>
          <br>
        <input
          type="password"
          name="password"
          v-model="password"
          placeholder="Password"/>
        <br>
        <button @click="login">Login</button>
    </div>
  </template>
  
  <script>
  import authenticationService from '../services/authentication'

  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      async login () {
      const response = await authenticationService.login({
        username: this.username,
        password: this.password
      })
        console.log(response.data)
      }
    }
  };
  </script>
  <style scoped>

</style>