<template>
  <nav>
    <v-toolbar app>
      <v-toolbar-side-icon @click="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>
        <span class="font-weight-light">Tool</span>
        <span>bar</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>

      <!-- Dropdown -->
      <v-menu offset-y="">
          <v-btn flat slot="activator" color="grey">
              <v-icon left>expand_more</v-icon>
              <span>menu</span>
          </v-btn>
          <v-list-tile class="white" v-for="link in links" :key="link.text" router :to="link.route">
              <v-list-tile-title>{{ link.text }}</v-list-tile-title>
          </v-list-tile>
      </v-menu>

      <v-btn flat>
        <span>Sign Out</span>
        <v-icon>exit_to_app</v-icon>
      </v-btn>
    </v-toolbar>

    <v-navigation-drawer app v-model="drawer" class="primary">
      <v-layout column align-center>
        <v-flex class="mt-5"></v-flex>
        <v-avatar size="100">
          <img src="/127860.jpg" alt>
        </v-avatar>
        <p class="white--text subheading mt-1">Do Minjun</p>
      </v-layout>
      <v-list>
        <v-list-tile v-for="link in links" :key="link.text" router :to="link.route">
          <v-list-tile-action>
            <v-icon class="white--text">{{ link.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title class="white--text">{{ link.text }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>


<script>
export default {
  data() {
    return {
      drawer: false,
      links: [
        { icon: "home", text: "Home", route: "/" },
        { icon: "folder", text: "My projects", route: "/projects" },
        { icon: "person", text: "Teams", route: "/teams" }
      ]
    };
  }
};
</script>