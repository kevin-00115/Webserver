<template>
  <el-container class="container">
    <el-header class="page-head">
      <div class="page-head-container">文本分析</div>
    </el-header>
    <el-container>
      <el-aside class="page-aside">
        <div class="page-aside-container">
          <el-menu class="page-aside-menu" :default-active="menu_active" :key="menu_active" @select="menu_select">
            <el-menu-item index="text_identi">文本分析</el-menu-item>
            <el-menu-item index="person_info">人员信息</el-menu-item>
            <el-menu-item index="case_info">事件信息</el-menu-item>
            <el-menu-item index="text_info">文本信息</el-menu-item>
          </el-menu>
        </div>
      </el-aside>
      <el-main class="page-main">
        <div class="page-main-container">
          <router-view @routeSwitch="menu_switch"></router-view>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>

export default {
  name: 'index',
  components: {
  },
  data() {
    return {
      menu_active: 'text_identi',
      curroutename: 'text_identi'
    }
  },
  watch: {
      curroutename: function(val) {
          this.menu_active = val
      }
  },
  methods: {
    menu_switch(route) {
        const idx = route.name
        this.curroutename = idx
    },
    menu_select(index){
        this.$router.push({name: index})
    }
  },
  created() {
    // console.log('created')
  }
}
</script>

<style>
:root, body, #app {
  height: 100%;
  width: 100%;
  margin: 0%;
}
.container {
  height: 100%;
  width: 100%;
}
.page-head {
  line-height: 60px;
  font-size: 20px;
  border-bottom: 1px solid #cbc8c8;
}
.page-head-container {
  padding: 0 32px;
  color: #409EFF;
}
.el-aside.page-aside {
  width: 200px;
}
.page-aside-container {
  height: 100%;
}
.el-menu.page-aside-menu {
  height: 100%;
}
.container .page-main {
  display: flex;
}
.page-main, .page-main-container {
  /* height: 100%; */
  display: flex;
  flex-direction: column;
  flex: 1;
}
</style>
