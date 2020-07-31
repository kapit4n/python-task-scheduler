import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../../shared/services/auth.service';
import { Router } from '@angular/router';
import { UsersService } from 'src/app/shared/services/users.service';

interface TokenRespI {
  token: string;
}

@Component({
  selector: 'app-sig-in',
  templateUrl: './sig-in.component.html',
  styleUrls: ['./sig-in.component.css']
})
export class SigInComponent implements OnInit {

  signInForm: FormGroup;

  constructor(private authService: AuthService,
    private userSvc: UsersService,
    private formBuilder: FormBuilder,
    private router: Router,) { }

  ngOnInit(): void {
    this.signInForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
    });
  }

  onSubmit() {
    const authValues = this.signInForm.value;
    this.authService.login(authValues).subscribe((res: TokenRespI) => {

      console.log(res);
      localStorage.setItem('token', res.access);
      this.userSvc.list().subscribe(data => console.log(data), err => console.log(err));
      // verify that we have a valid token
      //this.router.navigate(['home']);

      // this.authToken = res.token
    }, error => {
      console.error(error);
    })
  }

}
