<template>
      <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <v-btn 
          color="info" 
          flat fab large
          icon
          v-on="on">
          <v-icon>add</v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">{{$t('headlines.addPlayer')}}</span>
        </v-card-title>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap align-center justify-space-between>
              <v-flex xs3>
                <span>{{$t('table.name')}}:</span>
              </v-flex>
              <v-flex xs9>
                <v-text-field 
                v-model='newName'
                equired></v-text-field>
              </v-flex>
              <v-flex xs3>
                <span>{{$t('table.surname')}}:</span>
              </v-flex>
              <v-flex xs9>
                <v-text-field 
                v-model='newSurname'
                required></v-text-field>
              </v-flex>
              <v-flex xs3>
                <span>{{$t('table.dateOfBirth')}}:</span>
              </v-flex>
              <v-flex xs9>
                <v-menu
                  ref="birthMenu"
                  v-model="birthMenu"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  lazy
                  transition="scale-transition"
                  offset-y
                  full-width
                  max-width="290px"
                  min-width="290px"
                >
                  <template v-slot:activator="{ on }">
                    <v-text-field
                      v-model="date"
                      persistent-hint
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker v-model="date" no-title @input="birthMenu = false"></v-date-picker>
                </v-menu>
              </v-flex>
              <v-flex xs3>
                <span>{{$t('table.sex')}}:</span>
              </v-flex>
              <v-flex xs3>
                <v-select
                  :items="gender"
                  v-model="genderSelected"
                ></v-select>
              </v-flex>
              <v-flex xs3 text-xs-center>
                <span>{{$t('table.level')}}:</span>
              </v-flex>
              <v-flex xs3>
                <v-select
                  :items="level"
                  v-model='levelSelected'
                ></v-select>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="grey" flat fab large @click="dialog = false"><v-icon>close</v-icon></v-btn>
          <v-btn color="blue darken-1" flat fab large @click="saveToDb"><v-icon>save</v-icon></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>
<script>
import axios from "axios"
import { mapMutations } from 'vuex'
export default {
    data () {
      return {
        dialog: false,
        birthMenu: false,
        newName: '',
        newSurname: '',
        levelSelected: '',
        gender:['M','K'],
        genderSelected: '',
        date: '',
        headers: [
          { text: this.$t('table.name'), value: 'first_name', align: 'center'},
          { text: this.$t('table.surname'), value: 'last_name', align: 'center'},
          { text: this.$t('table.dateOfBirth'), value: 'date_of_birth', align: 'center'},
          { text: this.$t('table.sex'), value: 'sex', align: 'center'},
          { text: this.$t('table.kup'), value: 'level', align: 'center'},
        ],
        level: [
          '10 kup','9 kup','8 kup','7 kup','6 kup','5 kup','4 kup','3 kup','2 kup','1 kup', 
          '1 poom', '2 poom', '3 poom', 
          '1 dan', '2 dan', '3 dan', '4 dan', '5 dan', '6 dan', '7 dan', '8 dan', '9 dan', '10 dan',
        ],
        list: [],
      }
    },
    methods: {
      ...mapMutations({
        setSnackSuccess: 'snackbarsuccess/setSnack',
        setSnackError: 'snackbarerror/setSnack',
      }),
      saveToDb() {
        const dataToSend = {
          'name': this.newName,
          'surname': this.newSurname,
          'birthdate': this.date,
          'sex': this.genderSelected,
          'level': this.levelSelected,
        }
        axios.post("http://localhost:8000/send_data_list/", dataToSend).then(response => {
          this.setSnackSuccess(this.$t('snackbar.success'))
          window.location.reload(true)
        })
        .catch(error => {
          this.setSnackError(this.$t('snackbar.error'))
          console.error('error',error)
        });
        this.dialog = false
      }
    }
  }
</script>
