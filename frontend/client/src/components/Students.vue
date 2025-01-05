<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>books List</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>Add book</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">First Name</th>
              <th scope="col">Last Name</th>
              <th scope="col">Total Mark</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.books_name }}</td>
              <td>{{ book.author }}</td>
              <td>{{ book.year_creat }}</td>
              <!-- Add information that book was invited-->
              <!-- <td>
                <span v-if="book.invited">Yes</span>
                <span v-else>No</span>
              </td> -->
              <td>
                <div class="btn-group" role="group">
                  <button type="button" v-b-modal.book-update-modal @click="editbook(book)" class="btn btn-warning btn-sm">Update</button>
                  <button @click="onDeletebook(book)" type="button" class="btn btn-danger btn-sm" >Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addbookModal" id="book-modal" title="Add a new book" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-first-name-group" label="First Name:" label-for="form-first-name-input">
          <b-form-input id="form-first-name-input" type="text" v-model="addbookForm.firstName" required
            placeholder="Enter First Name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-last-name-group" label="Last Name:" label-for="form-last-name-input">
          <b-form-input id="form-last-name-input" type="text" v-model="addbookForm.lastName" required
            placeholder="Enter Last Name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-total-grade-group" label="Total Grade:" label-for="form-total-grade-input">
          <b-form-input id="form-total-grade-input" type="number" v-model="addbookForm.totalGrade" required
            placeholder="0">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editbookModal"
            id="book-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-first-name-edit-group"
                    label="First Name:"
                    label-for="form-first-name-edit-input">
          <b-form-input id="form-first-name-edit-input"
                        type="text"
                        v-model="editForm.firstName"
                        required
                        placeholder="Enter First Name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-last-name-edit-group"
                      label="Last Name:"
                      label-for="form-last-name-edit-input">
            <b-form-input id="form-last-name-edit-input"
                          type="text"
                          v-model="editForm.lastName"
                          required
                          placeholder="Enter Last Name">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-total-grade-edit-group"
                      label="Total Grade:"
                      label-for="form-total-grade-edit-input">
            <b-form-input id="form-total-grade-edit-input"
                          type="number"
                          v-model="editForm.totalGrade"
                          required
                          placeholder="0">
            </b-form-input>
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      books: [],
      addbookForm: {
        firstName: '',
        lastName: '',
        totalGrade: 0,
      },
      message: '',
      showMessage: false,
      editForm: {
        firstName: '',
        lastName: '',
        totalGrade: 0,
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getbooks() {
      const path = 'http://localhost:5000/books/';
      axios.get(path)
        .then((res) => {
          this.books = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addbook(payload) {
      const path = 'http://localhost:5000/books/';
      axios.post(path, payload)
        .then(() => {
          this.getbooks();
          this.message = 'book added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getbooks();
        });
    },
    initForm() {
      this.addbookForm.firstName = '';
      this.addbookForm.lastName = '';
      this.addbookForm.totalGrade = 0;
      this.editForm.bookID = 0;
      this.editForm.firstName = '';
      this.editForm.lastName = '';
      this.editForm.totalGrade = 0;
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addbookModal.hide();
      const payload = {
        books_name: this.addbookForm.firstName,
        author: this.addbookForm.lastName,
        year_creat: this.addbookForm.totalGrade,
      };
      this.addbook(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addbookModal.hide();
      this.initForm();
    },
    editbook(book) {
      this.editForm.bookID = book.book_id;
      this.editForm.firstName = book.books_name;
      this.editForm.lastName = book.author;
      this.editForm.totalGrade = book.year_creat;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editbookModal.hide();
      const payload = {
        book_id: this.editForm.bookID,
        books_name: this.editForm.firstName,
        author: this.editForm.lastName,
        year_creat: this.editForm.totalGrade,
      };
      this.updatebook(payload, this.editForm.bookID);
    },
    updatebook(payload, bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios.put(path, payload)
        .then((res) => {
          this.getbooks();
          this.message = res.data; //'book updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getbooks();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editbookModal.hide();
      this.initForm();
      this.getbooks();
    },
    removebook(bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios.delete(path)
        .then((res) => {
          this.getbooks();
          this.message = res.data;// 'book removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getbooks();
        });
    },
    onDeletebook(book) {
      this.removebook(book.book_id);
    },
  },
  created() {
    this.getbooks();
  },
};
</script>