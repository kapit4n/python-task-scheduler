import { Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { Task } from '../../shared/models/task'
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { TasksService } from 'src/app/shared/services/tasks.service';


@Component({
  selector: 'app-create-dialog',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css']
})
export class CreateComponentDialog implements OnInit {

  createForm: FormGroup;

  constructor(
    public dialogRef: MatDialogRef<CreateComponentDialog>,
    @Inject(MAT_DIALOG_DATA) public data: Task,
    private formBuilder: FormBuilder,
    private taskSvc: TasksService,
  ) {
  }

  ngOnInit(): void {
    this.createForm = this.formBuilder.group({
      description: ['', { validators: [Validators.required] }],
      status: [''],
      priority: [],
      estimated_time: [0],
      time: [0]
    });
  }

  onSubmit() {
    const taskInfo = this.createForm.value;
    this.taskSvc.create(taskInfo).subscribe(res => {
      console.log("Reload task list");
    });
    this.dialogRef.close();
  }

  onNoClick(): void {
    this.dialogRef.close();
  }

  onCancel(): void {
    this.createForm.reset();
    this.dialogRef.close();
  }

  get f() {
    return this.createForm.controls;
  }
}
