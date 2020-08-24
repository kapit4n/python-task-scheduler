import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Task } from '../models/task';
import { TaskLog } from '../models/taskLog';
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
    return this.http.post(`${BaseUrl}/api/tasks/`, taskInfo);
  }
  
  public createLog(taskLogInfo: TaskLog) {
    return this.http.post(`${BaseUrl}/api/task-logs/`, taskLogInfo);
  }

  public list() {
    return this.http.get<Task[]>(`${BaseUrl}/api/tasks/`);
  }
}
