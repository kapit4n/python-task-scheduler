import { Component, OnInit } from '@angular/core';

import { FormControl, Validators } from '@angular/forms';
import { UsersService } from 'src/app/shared/services/users.service';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';

interface IChangePasswordRequest {
  token: string;
  uidb64: string;
}

@Component({
  selector: 'app-reset-password-complete',
  templateUrl: './reset-password-complete.component.html',
  styleUrls: ['./reset-password-complete.component.css']
})
export class ResetPasswordCompleteComponent implements OnInit {
  token = '';
  password = 'admin02.,';
  uidb64 = '';
  url = '';


  passwordFormControl = new FormControl('', [
    Validators.required,
  ])

  constructor(private usrSvc: UsersService, private route: ActivatedRoute) { }

  onSubmit() {
    console.log("Call here service to reset password");
    const r = { token: this.token, password: this.password, uidb64: this.uidb64 };
    console.log(r);
    this.usrSvc.changePasswordComplete(r).subscribe(x => console.log(x));
  }

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      this.url = params['url'];
      this.usrSvc.changePasswordRequest(this.url).subscribe((res: IChangePasswordRequest) => {
        this.token = res.token;
        this.uidb64 = res.uidb64;
      })
    })
  }

}
