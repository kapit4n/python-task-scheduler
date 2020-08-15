import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { MaterialModule } from '../shared/material/material.module';
import { CreateComponentDialog } from './create/create.component';

@NgModule({
  declarations: [
    CreateComponentDialog,
  ],
  imports: [
    CommonModule,
    MaterialModule,
    ReactiveFormsModule,
  ],
  exports: [CreateComponentDialog]
})
export class TaskModule { }
