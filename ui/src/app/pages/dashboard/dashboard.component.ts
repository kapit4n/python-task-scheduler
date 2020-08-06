import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';

import { CreateComponentDialog } from '../../task/create/create.component';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  constructor(public dialog: MatDialog) {

  }

  openCreate() {
    const dialogRef = this.dialog.open(CreateComponentDialog);
    dialogRef.afterClosed().subscribe(result => {
      console.log(result);
    })

  }

  ngOnInit(): void {
  }

}
