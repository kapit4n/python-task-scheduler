import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Task } from '../models/task';
import { HttpClient } from '@angular/common/http';
import { BaseUrl } from '../base-url';

@Injectable({
  providedIn: 'root'
})
export class TasksService {

  constructor(
    private http: HttpClient,
  ) { }

  public create(taskInfo: Task) {
    return this.http.post('http://localhost:8000/api/tasks/', taskInfo);
  }
  public list() {
    return this.http.get<Task[]>('http://localhost:8000/api/tasks/');
  }
}
