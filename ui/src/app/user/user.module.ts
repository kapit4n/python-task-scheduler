import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RegisterComponent } from './register/register.component';
import { SigInComponent } from './sig-in/sig-in.component';
import { ReactiveFormsModule } from '@angular/forms';
import { MaterialModule } from '../shared/material/material.module';
import { ResetPasswordComponent } from './reset-password/reset-password.component';
import { ResetPasswordCompleteComponent } from './reset-password-complete/reset-password-complete.component';

@NgModule({
  declarations: [
    RegisterComponent,
    SigInComponent,
    ResetPasswordComponent,
    ResetPasswordCompleteComponent,
  ],
  imports: [
    CommonModule,
    MaterialModule,
    ReactiveFormsModule,
  ],
  exports: [RegisterComponent, ResetPasswordComponent, ResetPasswordCompleteComponent]
})
export class UserModule { }
