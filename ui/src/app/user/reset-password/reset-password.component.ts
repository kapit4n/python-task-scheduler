import { Component, OnInit } from '@angular/core';

import { FormControl, Validators } from '@angular/forms';
import { UsersService } from 'src/app/shared/services/users.service';


@Component({
  selector: 'app-reset-password',
  templateUrl: './reset-password.component.html',
  styleUrls: ['./reset-password.component.css']
})
export class ResetPasswordComponent implements OnInit {
  emailFormControl = new FormControl('', [
    Validators.required,
  ])

  constructor(private usrSvc: UsersService) { }

  onSubmit() {
    console.log("Call here service to reset password");
    this.usrSvc.requestChangePasswordEmail({ email: 'luis.arce22@gmail.com' }).subscribe(x => console.log(x));
  }

  ngOnInit(): void {
  }

}
