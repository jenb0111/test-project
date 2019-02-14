<template>
  <div class="teams">
    <h1>Hello!! There are teams.</h1>
    <v-container class="my-5">

      <!-- grid system -->
      <v-layout row wrap>
        <v-flex xs12 md6>
          <v-btn outline block>1</v-btn>
        </v-flex>
        <v-flex xs4 md6>
          <v-btn outline block>2</v-btn>
        </v-flex>
        <v-flex xs4 md6>
          <v-btn outline block>2</v-btn>
        </v-flex>
        <v-flex xs4 md6>
          <v-btn outline block>2</v-btn>
        </v-flex>
      </v-layout>

      <v-layout row wrap justify-space-around>
        <v-flex xs4 md3>
          <v-btn outline block class="success">1</v-btn>
        </v-flex>
        <v-flex xs4 md3>
          <v-btn outline block>1</v-btn>
        </v-flex>
      </v-layout>

      <v-layout row class="my-5">
        <v-btn small flat color="grey" @click="sortBy('title')">
          <v-icon left small>folder</v-icon>
          <span class="caption text-lowercase">By project name</span>
        </v-btn>
        <v-btn small flat color="grey" @click="sortBy('person')">
          <v-icon left small>person</v-icon>
          <span class="caption text-lowercase">By person</span>
        </v-btn>
      </v-layout>

       <v-card flat class="pa-3" v-for="project in projects" :key="project.tile">
        <v-layout row wrap :class="`pa-3 project ${project.status}`">
          <v-flex xs12 md5>
            <div class="caption grey--text">Project title</div>
            <div>{{ project.title }}</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Person</div>
            <div>{{ project.person }}</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Due by</div>
            <div>{{ project.duedate }}</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Status</div>
            <div><v-chip small :class="`${project.status} white--text caption my-2`">{{ project.status }}</v-chip></div>
          </v-flex>
        </v-layout>
        <v-divider></v-divider>
      </v-card>

       <v-card flat class="pa-3">
        <v-layout row wrap>
          <v-flex xs12 md5>
            <div class="caption grey--text">Project title</div>
            <div>Create a new website</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Person</div>
            <div>Plaifah Atthapaibul</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Due by</div>
            <div>Jan 1st, 2019</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Status</div>
            <div>Ongoing</div>
          </v-flex>
        </v-layout>
      </v-card>

    </v-container>
  </div>
</template>

<script>  
  export default {
    data() {
      return {
        projects: [
        { title: 'Design a new website', person: 'Plaifah Atthapaibul', duedate: 'Jan 11th, 2019', status: 'ongoing', content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet ipsam voluptatibus harum aspernatur saepe quod minima quibusdam voluptate corporis asperiores consectetur vero assumenda blanditiis possimus veniam officia, odio aut consequuntur.'},
        { title: 'Coding', person: 'Do Minjun', duedate: 'Jan 1st, 2019', status: 'complete', content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet ipsam voluptatibus harum aspernatur saepe quod minima quibusdam voluptate corporis asperiores consectetur vero assumenda blanditiis possimus veniam officia, odio aut consequuntur.' },
        { title: 'Design xxx', person: 'Natcha Likitrungsan', duedate: 'March 8th, 2019', status: 'complete', contend: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet ipsam voluptatibus harum aspernatur saepe quod minima quibusdam voluptate corporis asperiores consectetur vero assumenda blanditiis possimus veniam officia, odio aut consequuntur.'},
        { title: 'Create a community forum', person: 'Im Jaebum', duedate: 'Jan 6th, 2019', status: 'overdue', content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet ipsam voluptatibus harum aspernatur saepe quod minima quibusdam voluptate corporis asperiores consectetur vero assumenda blanditiis possimus veniam officia, odio aut consequuntur.'}
      ]
      }
    },
    methods: {
      sortBy(prop){
        this.projects.sort((a,b) => a[prop] < b[prop] ? -1 : 1)
      }
    }

  }
</script>

<style>

.project.complete {
  border-left: 4px solid #3cd1c2;
}
.project.ongoing {
  border-left: 4px solid orange
}
.project.overdue{
  border-left: 4px solid tomato;
}
.v-chip.complete {
  background: #3cd1c2;
}
.v-chip.ongoing {
  background: orange
}
.v-chip.overdue{
  background: tomato;
}
</style>

