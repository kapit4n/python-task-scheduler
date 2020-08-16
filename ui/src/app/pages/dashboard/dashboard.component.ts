import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Task } from '../../shared/models/task'
import { TasksService } from 'src/app/shared/services/tasks.service';

import { CreateComponentDialog } from '../../task/create/create.component';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  tasks:Task[] = []
  constructor(public dialog: MatDialog,
    private _tastsService: TasksService
    ) {    
  }

  openCreate() {
    const dialogRef = this.dialog.open(CreateComponentDialog);
    dialogRef.afterClosed().subscribe(result => {
      console.log(result);
    })

  }

  ngOnInit(): void {
    this._tastsService.list()
      .subscribe(tasks => {
        this.tasks = tasks;
      });
  }

}
