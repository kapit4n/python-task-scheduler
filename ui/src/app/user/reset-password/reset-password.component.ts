import { Component, OnInit } from '@angular/core';

import { FormControl, Validators } from '@angular/forms';


@Component({
  selector: 'app-reset-password',
  templateUrl: './reset-password.component.html',
  styleUrls: ['./reset-password.component.css']
})
export class ResetPasswordComponent implements OnInit {
  emailFormControl = new FormControl('', [
    Validators.required,
    Validators.email,
  ])

  constructor() { }

  onSubmit() {
    console.log("Call here service to reset password");

  }

  ngOnInit(): void {
  }

}
