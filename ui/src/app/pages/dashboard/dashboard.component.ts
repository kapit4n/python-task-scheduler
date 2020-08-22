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
  tasks: Task[] = []
  current: Task;
  totalTime = 0;
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
        // call endpoint the get the current stask
        this.tasks.forEach(element => {
          if (element.status === 'progress') {
            this.current = element;
          }
        });
        this.startTimer();

      });
  }

  continueCurrent() {
    this.current.status = 'pending';
  }

  startCurrent() {
    this.current.status = 'progress';
  }

  finishCurrent() {
    this.current.status = 'finished';
  }

  startTimer() {
    setInterval(() => {
      if (this.current && this.current.status == 'progress') {
        this.current.time = this.current.time + 1;
        let total = 0;
        this.tasks.forEach(element => {
          total = total + element.time;
        });
        this.totalTime = total;
      }
    }, 1000)
  }

  continueTask(task) {
    task.status = 'pending';
  }

  startTask(task) {
    this.tasks.forEach(element => {
      if (element.status === 'progress') {
        element.status = 'pending';
      }
    });
    task.status = 'progress';
    this.current = task;
  }

  finishTask(task) {
    task.status = 'finished';
  }
}
