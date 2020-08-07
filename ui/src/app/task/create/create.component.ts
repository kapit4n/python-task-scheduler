import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { Task } from '../../shared/models/task'

@Component({
  selector: 'app-create-dialog',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css']
})
export class CreateComponentDialog {

  

  constructor(
    public dialogRef: MatDialogRef<CreateComponentDialog>,
    @Inject(MAT_DIALOG_DATA) public data: Task) {

  }

  onNoClick(): void {
    this.dialogRef.close();
  }
}
