import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RegisterComponent } from './register/register.component';
import { ResetPasswordComponent } from './reset-password/reset-password.component';


@NgModule({
  declarations: [RegisterComponent, ResetPasswordComponent],
  imports: [
    CommonModule
  ],
  exports: [RegisterComponent]
})
export class ClientModule { }
